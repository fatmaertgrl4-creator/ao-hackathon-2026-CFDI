#!/usr/bin/env python3
"""Alarm korelasyon uygulamasi.

Verilen alarm CSV dosyasini tamamen okur, alarm firtinasini olay kartlarina
indirger ve ayni giris noktasindan web demo arayuzu sunar.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse


CRITICAL_ROOT_TYPES = {
    "network_down",
    "pkt_loss",
    "disk_full",
    "db_write_fail",
    "db_conn_pool",
    "txn_fail",
    "conn_refused",
    "http_5xx",
    "timeout",
    "thread_pool",
    "oom_risk",
    "ext_slow",
}

NOISE_TYPES = {
    "backup_warn",
    "cert_expiry",
    "disk_warn",
    "log_rotate",
    "ntp_drift",
    "cpu_high",
    "mem_high",
}

NETWORK_TYPES = {"network_down", "pkt_loss", "network_flap"}
DB_TYPES = {"disk_full", "db_write_fail", "db_conn_pool"}
SERVICE_IMPACT_TYPES = {"txn_fail", "conn_refused", "http_5xx", "timeout", "thread_pool", "latency_high", "ext_slow"}
ROOT_WEIGHT = {
    "network_down": 9,
    "pkt_loss": 8,
    "disk_full": 9,
    "db_write_fail": 8,
    "db_conn_pool": 7,
    "txn_fail": 6,
    "conn_refused": 6,
    "http_5xx": 5,
    "timeout": 5,
    "thread_pool": 4,
    "ext_slow": 5,
    "oom_risk": 5,
    "latency_high": 3,
}

TARGET_PATTERNS = (
    re.compile(r"([a-z0-9-]+) servisine", re.IGNORECASE),
    re.compile(r"([a-z0-9-]+) baglantisi", re.IGNORECASE),
)


@dataclass(frozen=True)
class Alarm:
    alarm_id: str
    timestamp: datetime
    source_system: str
    host: str
    service: str
    severity: int
    alarm_type: str
    message: str
    veri_merkezi: str
    kabin: str
    ortam: str
    target_service: str | None
    raw: dict[str, str]


@dataclass
class WorkingCluster:
    cluster_id: str
    category: str
    locus: str
    seed: Alarm
    alarms: list[Alarm] = field(default_factory=list)


CriticalityRank = {"dusuk": 1, "orta": 2, "yuksek": 3, "kritik": 4}


def default_data_path() -> Path:
    candidates = [
        Path("data/alarms.csv"),
        Path("../katilimci_paketi/alarms.csv"),
        Path("/Users/TCNGUNDUZ/Downloads/katilimci_paketi/alarms.csv"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def default_dependency_path() -> Path:
    candidates = [
        Path("data/service_dependencies.csv"),
        Path("../katilimci_paketi/service_dependencies.csv"),
        Path("/Users/TCNGUNDUZ/Downloads/katilimci_paketi/service_dependencies.csv"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def default_inventory_path() -> Path:
    candidates = [
        Path("data/host_inventory.csv"),
        Path("../katilimci_paketi/host_inventory.csv"),
        Path("/Users/TCNGUNDUZ/Downloads/katilimci_paketi/host_inventory.csv"),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


def load_dependencies(path: Path | None) -> dict[str, Any]:
    graph: dict[str, Any] = {"by_source": defaultdict(list), "by_target": defaultdict(list), "edges": set(), "rows": []}
    if path is None or not path.exists():
        return graph

    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            item = {
                "source": row["kaynak_servis"],
                "target": row["hedef_servis"],
                "type": row["bagimlilik_tipi"],
                "criticality": row["kritiklik"],
            }
            graph["rows"].append(item)
            graph["by_source"][item["source"]].append(item)
            graph["by_target"][item["target"]].append(item)
            graph["edges"].add((item["source"], item["target"]))
    return graph


def load_inventory(path: Path | None) -> dict[str, Any]:
    inventory: dict[str, Any] = {"hosts": {}, "service_hosts": defaultdict(list), "service_criticality": {}}
    if path is None or not path.exists():
        return inventory

    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            host_info = {
                "host": row["host"],
                "service": row["servis"],
                "data_center": row["veri_merkezi"],
                "rack": row["kabin"],
                "environment": row["ortam"],
                "criticality": row["is_kritikligi"],
            }
            inventory["hosts"][row["host"]] = host_info
            inventory["service_hosts"][row["servis"]].append(host_info)
            current = inventory["service_criticality"].get(row["servis"], "dusuk")
            if CriticalityRank.get(row["is_kritikligi"], 0) > CriticalityRank.get(current, 0):
                inventory["service_criticality"][row["servis"]] = row["is_kritikligi"]
    return inventory


def parse_target_service(message: str) -> str | None:
    for pattern in TARGET_PATTERNS:
        match = pattern.search(message)
        if match:
            return match.group(1)
    return None


def load_alarms(path: Path) -> list[Alarm]:
    if not path.exists():
        raise FileNotFoundError(f"Alarm dosyasi bulunamadi: {path}")

    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))

    required_columns = {
        "alarm_id",
        "timestamp",
        "source_system",
        "host",
        "service",
        "severity",
        "alarm_type",
        "message",
        "veri_merkezi",
        "kabin",
        "ortam",
    }
    missing = required_columns - set(rows[0].keys() if rows else [])
    if missing:
        raise ValueError(f"CSV kolonlari eksik: {', '.join(sorted(missing))}")

    alarms: list[Alarm] = []
    for row in rows:
        alarms.append(
            Alarm(
                alarm_id=row["alarm_id"],
                timestamp=datetime.fromisoformat(row["timestamp"]),
                source_system=row["source_system"],
                host=row["host"],
                service=row["service"],
                severity=int(row["severity"]),
                alarm_type=row["alarm_type"],
                message=row["message"],
                veri_merkezi=row["veri_merkezi"],
                kabin=row["kabin"],
                ortam=row["ortam"],
                target_service=parse_target_service(row["message"]),
                raw=row,
            )
        )
    return sorted(alarms, key=lambda alarm: alarm.timestamp)


def classify_alarm(alarm: Alarm) -> tuple[str, str]:
    if alarm.alarm_type in NETWORK_TYPES and alarm.severity >= 4:
        return "network", f"{alarm.veri_merkezi}/{alarm.kabin}"
    if alarm.alarm_type in DB_TYPES or ("db" in alarm.service and alarm.alarm_type in {"disk_warn", "disk_full"}):
        return "database", alarm.service
    if alarm.alarm_type in SERVICE_IMPACT_TYPES:
        target = alarm.target_service or alarm.service
        return "service", target
    if alarm.alarm_type in {"gc_pressure", "oom_risk"}:
        return "runtime", alarm.service
    return "resource", alarm.service


def root_score(alarm: Alarm, local_density: int) -> float:
    weight = ROOT_WEIGHT.get(alarm.alarm_type, 1)
    if alarm.alarm_type in NOISE_TYPES and alarm.severity <= 3:
        weight -= 2
    return (alarm.severity * 2.0) + weight + min(local_density, 10) * 0.6


def density_by_key(alarms: list[Alarm], window: timedelta) -> dict[str, int]:
    buckets: dict[str, int] = {}
    for alarm in alarms:
        category, locus = classify_alarm(alarm)
        key = f"{category}:{locus}:{alarm.timestamp.replace(second=0, microsecond=0).isoformat()}"
        buckets[key] = 0

    for alarm in alarms:
        category, locus = classify_alarm(alarm)
        nearby = 0
        for other in alarms:
            if abs((other.timestamp - alarm.timestamp).total_seconds()) > window.total_seconds():
                continue
            other_category, other_locus = classify_alarm(other)
            if other_category == category and other_locus == locus:
                nearby += 1
        buckets[f"{category}:{locus}:{alarm.alarm_id}"] = nearby
    return buckets


def seed_clusters(alarms: list[Alarm]) -> list[WorkingCluster]:
    density = density_by_key(alarms, timedelta(minutes=4))
    candidates: list[tuple[float, Alarm, str, str]] = []
    for alarm in alarms:
        category, locus = classify_alarm(alarm)
        local_density = density[f"{category}:{locus}:{alarm.alarm_id}"]
        score = root_score(alarm, local_density)
        if alarm.severity >= 5 or (alarm.severity >= 4 and alarm.alarm_type in CRITICAL_ROOT_TYPES) or score >= 15:
            candidates.append((score, alarm, category, locus))

    candidates.sort(key=lambda item: (-item[0], item[1].timestamp))
    clusters: list[WorkingCluster] = []
    for _score, alarm, category, locus in candidates:
        if any(abs((cluster.seed.timestamp - alarm.timestamp).total_seconds()) <= 360 and cluster.category == category and cluster.locus == locus for cluster in clusters):
            continue
        if category != "network" and any(
            cluster.category == "network"
            and cluster.locus == f"{alarm.veri_merkezi}/{alarm.kabin}"
            and -180 <= (alarm.timestamp - cluster.seed.timestamp).total_seconds() <= 1200
            for cluster in clusters
        ):
            continue
        cluster_id = f"OLAY-{len(clusters) + 1:02d}"
        clusters.append(WorkingCluster(cluster_id=cluster_id, category=category, locus=locus, seed=alarm, alarms=[alarm]))
        if len(clusters) >= 15:
            break
    return sorted(clusters, key=lambda cluster: cluster.seed.timestamp)


def dependency_boost(alarm: Alarm, cluster: WorkingCluster, dependencies: dict[str, Any]) -> float:
    seed_service = cluster.seed.service
    candidate_roots = {seed_service, cluster.locus}
    score = 0.0
    for root in candidate_roots:
        if (alarm.service, root) in dependencies["edges"]:
            score += 4
        if (root, alarm.service) in dependencies["edges"]:
            score += 2
        if alarm.target_service and (alarm.service, alarm.target_service) in dependencies["edges"]:
            score += 2
        if alarm.target_service and alarm.target_service == root:
            score += 3
    return score


def correlation_score(alarm: Alarm, cluster: WorkingCluster, dependencies: dict[str, Any] | None = None) -> float:
    seed = cluster.seed
    delta_minutes = (alarm.timestamp - seed.timestamp).total_seconds() / 60
    if delta_minutes < -3 or delta_minutes > 22:
        return -100

    score = 0.0
    if -1 <= delta_minutes <= 12:
        score += 3
    elif delta_minutes > 12:
        score += 1

    category, locus = classify_alarm(alarm)
    if category == cluster.category and locus == cluster.locus:
        score += 6
    if alarm.service == seed.service:
        score += 5
    if alarm.target_service and alarm.target_service == seed.service:
        score += 5
    if alarm.target_service and alarm.target_service == cluster.locus:
        score += 4
    if alarm.veri_merkezi == seed.veri_merkezi and alarm.kabin == seed.kabin:
        score += 4
    elif alarm.veri_merkezi == seed.veri_merkezi:
        score += 1
    if alarm.alarm_type in CRITICAL_ROOT_TYPES:
        score += 1
    if cluster.category == "network" and alarm.veri_merkezi == seed.veri_merkezi and alarm.kabin == seed.kabin:
        score += 4
    if cluster.category == "database" and ("billing" in alarm.service or alarm.target_service == seed.service):
        score += 4
    if cluster.category == "service" and (alarm.service == cluster.locus or alarm.target_service == cluster.locus):
        score += 4
    if dependencies:
        score += dependency_boost(alarm, cluster, dependencies)
    if alarm.alarm_type in NOISE_TYPES and alarm.severity <= 2:
        score -= 2
    return score


def assign_alarms(alarms: list[Alarm], clusters: list[WorkingCluster], dependencies: dict[str, Any] | None = None) -> set[str]:
    assigned: set[str] = {cluster.seed.alarm_id for cluster in clusters}
    for alarm in alarms:
        if alarm.alarm_id in assigned:
            continue
        scored = [(correlation_score(alarm, cluster, dependencies), cluster) for cluster in clusters]
        best_score, best_cluster = max(scored, key=lambda item: item[0])
        threshold = 5 if alarm.severity >= 4 else 7
        if best_score >= threshold:
            best_cluster.alarms.append(alarm)
            assigned.add(alarm.alarm_id)
    return assigned


def cluster_time_range(cluster: WorkingCluster) -> tuple[datetime, datetime]:
    times = [alarm.timestamp for alarm in cluster.alarms]
    return min(times), max(times)


def alarm_family(alarm_type: str) -> str:
    if alarm_type in NETWORK_TYPES:
        return "network"
    if alarm_type in DB_TYPES:
        return "database"
    if alarm_type in {"txn_fail", "http_5xx", "timeout", "conn_refused", "thread_pool", "latency_high"}:
        return "service-impact"
    return alarm_type


def should_merge_clusters(left: WorkingCluster, right: WorkingCluster) -> bool:
    if left.category != right.category or left.locus != right.locus:
        return False
    if alarm_family(left.seed.alarm_type) != alarm_family(right.seed.alarm_type):
        return False

    left_start, left_end = cluster_time_range(left)
    right_start, right_end = cluster_time_range(right)
    gap = (right_start - left_end).total_seconds() / 60
    overlap = right_start <= left_end and left_start <= right_end
    return overlap or 0 <= gap <= 12


def consolidate_related_clusters(clusters: list[WorkingCluster]) -> list[WorkingCluster]:
    ordered = sorted(clusters, key=lambda cluster: cluster_time_range(cluster)[0])
    merged: list[WorkingCluster] = []
    for cluster in ordered:
        target = next((candidate for candidate in merged if should_merge_clusters(candidate, cluster)), None)
        if target is None:
            merged.append(cluster)
            continue

        by_alarm_id = {alarm.alarm_id: alarm for alarm in target.alarms}
        for alarm in cluster.alarms:
            by_alarm_id.setdefault(alarm.alarm_id, alarm)
        target.alarms = sorted(by_alarm_id.values(), key=lambda alarm: alarm.timestamp)
        if root_score(cluster.seed, len(cluster.alarms)) > root_score(target.seed, len(target.alarms)):
            target.seed = cluster.seed

    for index, cluster in enumerate(merged, start=1):
        cluster.cluster_id = f"OLAY-{index:02d}"
    return merged


def summarize_action(category: str, locus: str, root_type: str) -> str:
    if category == "network":
        return f"{locus} icin switch/port ve uplink sagligini kontrol et; ayni raftaki kritik servisleri izole et."
    if category == "database" and root_type == "disk_full":
        return f"{locus} tablespace/disk dolulugunu temizle veya genislet; yazma hatalarini yeniden dene."
    if category == "database":
        return f"{locus} veritabani yazma ve baglanti havuzu kapasitesini kontrol et."
    if category == "service":
        return f"{locus} servisinin bagimliliklarini ve hata oranini kontrol et; gerekirse trafik azalt."
    if category == "runtime":
        return f"{locus} JVM/worker bellek ve GC baskisini kontrol et."
    return f"{locus} uzerindeki kaynak alarmlarini dogrula ve kapasiteyi kontrol et."


def owner_for(category: str, locus: str) -> str:
    if category == "network":
        return "NOC / Network"
    if category == "database":
        return "DBA"
    if category == "service":
        return "Servis Sahibi"
    if category == "runtime":
        return "Platform"
    return "SRE"


def root_hypothesis(cluster: WorkingCluster) -> str:
    alarm = cluster.seed
    if cluster.category == "network":
        return f"{cluster.locus} lokasyonunda ag erisim problemi ({alarm.alarm_type})"
    if cluster.category == "database":
        return f"{cluster.locus} veritabani kapasite/yazma problemi ({alarm.alarm_type})"
    if cluster.category == "service":
        return f"{cluster.locus} servis veya bagimlilik hatasi ({alarm.alarm_type})"
    if cluster.category == "runtime":
        return f"{cluster.locus} calisma zamani kaynak baskisi ({alarm.alarm_type})"
    return f"{cluster.locus} kaynak anomalisi ({alarm.alarm_type})"


def explain_cluster(cluster: WorkingCluster) -> tuple[str, list[str], list[str], float]:
    alarms = sorted(cluster.alarms, key=lambda alarm: alarm.timestamp)
    type_counts = Counter(alarm.alarm_type for alarm in alarms)
    service_counts = Counter(alarm.service for alarm in alarms)
    location_counts = Counter((alarm.veri_merkezi, alarm.kabin) for alarm in alarms)
    max_severity = max(alarm.severity for alarm in alarms)
    root_first = cluster.seed.timestamp == alarms[0].timestamp
    affected = len(service_counts)
    root_type_count = type_counts[cluster.seed.alarm_type]

    reasons = [
        f"Ilk guclu sinyal {cluster.seed.timestamp.isoformat(timespec='seconds')} zamaninda {cluster.seed.service} uzerinde {cluster.seed.alarm_type} olarak geldi.",
        f"Ayni korelasyon penceresinde {len(alarms)} alarm, {affected} servis ve {len(location_counts)} lokasyon gozlemlendi.",
        f"Baskin alarm tipleri: {', '.join(f'{name}={count}' for name, count in type_counts.most_common(4))}.",
    ]
    if location_counts:
        location, count = location_counts.most_common(1)[0]
        reasons.append(f"En yogun lokasyon {location[0]}/{location[1]} ve bu lokasyonda {count} alarm var.")

    counter_possibilities = []
    if cluster.category == "network":
        counter_possibilities.extend([
            "Tekil servis deploy veya thread havuzu problemi ag alarmi gibi gorunmus olabilir.",
            "Izleme sistemlerinden biri ayni fiziksel arizayi tekrarli raporlamis olabilir.",
        ])
    elif cluster.category == "database":
        counter_possibilities.extend([
            "Uygulama tarafindaki trafik artisi veritabani kapasite sinyalini tetiklemiş olabilir.",
            "Disk dolulugu ile islem hatalari ayni anda gorulse de arada kesin nedensellik elle dogrulanmalidir.",
        ])
    else:
        counter_possibilities.extend([
            "Bagimli servislerden gelen hata dalgasi asil nedeni bu servis gibi gosterebilir.",
            "Ayni zaman penceresindeki bagimsiz alarm gurultusu skorlamaya karismis olabilir.",
        ])

    confidence = 0.45 + min(len(alarms), 80) / 200 + min(max_severity, 5) * 0.04 + min(root_type_count, 8) * 0.02
    if root_first:
        confidence += 0.08
    if cluster.category in {"network", "database"}:
        confidence += 0.08
    confidence = round(min(confidence, 0.95), 2)
    return " ".join(reasons), reasons, counter_possibilities, confidence


def find_similar_patterns(cluster: WorkingCluster, all_alarms: list[Alarm]) -> list[str]:
    seed = cluster.seed
    before = [alarm for alarm in all_alarms if alarm.timestamp < seed.timestamp]
    if not before:
        return []

    service_counts = Counter(
        alarm.service
        for alarm in before
        if alarm.service in {member.service for member in cluster.alarms} and alarm.alarm_type in {member.alarm_type for member in cluster.alarms}
    )
    location_counts = Counter(
        f"{alarm.veri_merkezi}/{alarm.kabin}"
        for alarm in before
        if alarm.veri_merkezi == seed.veri_merkezi and alarm.kabin == seed.kabin and alarm.alarm_type in {member.alarm_type for member in cluster.alarms}
    )
    patterns = []
    if service_counts:
        service, count = service_counts.most_common(1)[0]
        patterns.append(f"Gecmis pencerede {service} icin benzer alarm tipi {count} kez goruldu.")
    if location_counts:
        location, count = location_counts.most_common(1)[0]
        patterns.append(f"Ayni lokasyon ({location}) daha once {count} benzer alarm uretmis.")
    return patterns[:2]


def service_criticality(service: str, inventory: dict[str, Any]) -> str:
    return inventory.get("service_criticality", {}).get(service, "bilinmiyor")


def alarm_row(alarm: Alarm, inventory: dict[str, Any]) -> dict[str, Any]:
    host_info = inventory.get("hosts", {}).get(alarm.host, {})
    return {
        "alarm_id": alarm.alarm_id,
        "timestamp": alarm.timestamp.isoformat(timespec="seconds"),
        "source_system": alarm.source_system,
        "host": alarm.host,
        "service": alarm.service,
        "service_criticality": service_criticality(alarm.service, inventory),
        "host_criticality": host_info.get("criticality", "bilinmiyor"),
        "severity": alarm.severity,
        "alarm_type": alarm.alarm_type,
        "target_service": alarm.target_service,
        "location": f"{alarm.veri_merkezi}/{alarm.kabin}",
        "message": alarm.message,
    }


def service_groups(alarms: list[Alarm], inventory: dict[str, Any]) -> list[dict[str, Any]]:
    grouped: dict[str, list[Alarm]] = defaultdict(list)
    for alarm in alarms:
        grouped[alarm.service].append(alarm)
    result = []
    for service, service_alarms in grouped.items():
        result.append(
            {
                "service": service,
                "criticality": service_criticality(service, inventory),
                "alarm_count": len(service_alarms),
                "max_severity": max(alarm.severity for alarm in service_alarms),
                "top_alarm_types": Counter(alarm.alarm_type for alarm in service_alarms).most_common(4),
                "hosts": sorted({alarm.host for alarm in service_alarms}),
                "locations": sorted({f"{alarm.veri_merkezi}/{alarm.kabin}" for alarm in service_alarms}),
            }
        )
    return sorted(result, key=lambda item: (-CriticalityRank.get(item["criticality"], 0), -item["max_severity"], -item["alarm_count"], item["service"]))


def dependency_impact(cluster: WorkingCluster, affected_services: list[str], dependencies: dict[str, Any]) -> dict[str, Any]:
    roots = {cluster.seed.service, cluster.locus}
    direct_upstream = []
    direct_downstream = []
    for root in roots:
        direct_upstream.extend(dependencies["by_target"].get(root, []))
        direct_downstream.extend(dependencies["by_source"].get(root, []))
    observed_upstream = [item for item in direct_upstream if item["source"] in affected_services]
    observed_downstream = [item for item in direct_downstream if item["target"] in affected_services]
    return {
        "direct_upstream": direct_upstream,
        "direct_downstream": direct_downstream,
        "observed_upstream": observed_upstream,
        "observed_downstream": observed_downstream,
    }


def build_event_card(cluster: WorkingCluster, all_alarms: list[Alarm], dependencies: dict[str, Any], inventory: dict[str, Any]) -> dict[str, Any]:
    alarms = sorted(cluster.alarms, key=lambda alarm: alarm.timestamp)
    affected_services = sorted({alarm.service for alarm in alarms})
    type_counts = Counter(alarm.alarm_type for alarm in alarms)
    source_counts = Counter(alarm.source_system for alarm in alarms)
    severity_counts = Counter(str(alarm.severity) for alarm in alarms)
    explanation, reasons, counter_possibilities, confidence = explain_cluster(cluster)
    start = alarms[0].timestamp
    end = alarms[-1].timestamp
    action_id = f"ACT-{cluster.cluster_id.split('-')[-1]}"

    return {
        "id": cluster.cluster_id,
        "root_hypothesis": root_hypothesis(cluster),
        "category": cluster.category,
        "locus": cluster.locus,
        "root_alarm": cluster.seed.alarm_id,
        "root_alarm_type": cluster.seed.alarm_type,
        "affected_services": affected_services,
        "service_groups": service_groups(alarms, inventory),
        "grouped_alarms": [alarm_row(alarm, inventory) for alarm in alarms],
        "dependency_impact": dependency_impact(cluster, affected_services, dependencies),
        "alarm_count": len(alarms),
        "time_range": {
            "start": start.isoformat(timespec="seconds"),
            "end": end.isoformat(timespec="seconds"),
            "minutes": round((end - start).total_seconds() / 60, 1),
        },
        "max_severity": max(alarm.severity for alarm in alarms),
        "explanation": explanation,
        "reasons": reasons,
        "counter_possibilities": counter_possibilities,
        "confidence": confidence,
        "evidence": {
            "top_alarm_types": type_counts.most_common(6),
            "source_systems": source_counts.most_common(),
            "severity_distribution": sorted(severity_counts.items()),
            "sample_alarm_ids": [alarm.alarm_id for alarm in alarms[:8]],
        },
        "similar_patterns": find_similar_patterns(cluster, all_alarms),
        "action": {
            "id": action_id,
            "title": summarize_action(cluster.category, cluster.locus, cluster.seed.alarm_type),
            "owner": owner_for(cluster.category, cluster.locus),
            "status": "acik",
        },
    }


def noise_reason(alarm: Alarm, clusters: list[WorkingCluster], dependencies: dict[str, Any]) -> str:
    scores = [correlation_score(alarm, cluster, dependencies) for cluster in clusters]
    best = max(scores) if scores else 0
    if alarm.alarm_type in NOISE_TYPES and alarm.severity <= 2:
        return "Dusuk siddetli bakim/kaynak uyarisi ve olay skoru esigin altinda."
    if best < 5:
        return "Zaman, servis veya lokasyon bagi guclu bir olay kartina yetmedi."
    return "En yakin olay kartina atama esigini gecemedi."


def build_noise_audit(alarms: list[Alarm], assigned: set[str], clusters: list[WorkingCluster], dependencies: dict[str, Any], inventory: dict[str, Any]) -> dict[str, Any]:
    noise = [alarm for alarm in alarms if alarm.alarm_id not in assigned]
    by_type = Counter(alarm.alarm_type for alarm in noise)
    by_service = Counter(alarm.service for alarm in noise)
    samples = [
        {
            "alarm_id": alarm.alarm_id,
            "timestamp": alarm.timestamp.isoformat(timespec="seconds"),
            "service": alarm.service,
            "service_criticality": service_criticality(alarm.service, inventory),
            "severity": alarm.severity,
            "alarm_type": alarm.alarm_type,
            "reason": noise_reason(alarm, clusters, dependencies),
        }
        for alarm in noise[:80]
    ]
    return {
        "count": len(noise),
        "by_type": by_type.most_common(12),
        "by_service": by_service.most_common(12),
        "samples": samples,
    }


def analyze(path: Path, dependency_path: Path | None = None, inventory_path: Path | None = None) -> dict[str, Any]:
    alarms = load_alarms(path)
    dependencies = load_dependencies(dependency_path)
    inventory = load_inventory(inventory_path)
    clusters = seed_clusters(alarms)
    assigned = assign_alarms(alarms, clusters, dependencies)
    clusters = consolidate_related_clusters(clusters)
    cards = [build_event_card(cluster, alarms, dependencies, inventory) for cluster in clusters]
    cards.sort(key=lambda card: (-card["max_severity"], card["time_range"]["start"], -card["alarm_count"]))

    for index, card in enumerate(cards, start=1):
        card["priority"] = index
        card["action"]["id"] = f"ACT-{index:02d}"

    total = len(alarms)
    return {
        "data_path": str(path),
        "dependency_path": str(dependency_path) if dependency_path and dependency_path.exists() else None,
        "inventory_path": str(inventory_path) if inventory_path and inventory_path.exists() else None,
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "summary": {
            "total_alarms": total,
            "event_cards": len(cards),
            "reduction_ratio": round(len(cards) / total, 5) if total else 0,
            "noise_count": total - len(assigned),
            "time_range": {
                "start": alarms[0].timestamp.isoformat(timespec="seconds") if alarms else None,
                "end": alarms[-1].timestamp.isoformat(timespec="seconds") if alarms else None,
            },
            "top_alarm_types": Counter(alarm.alarm_type for alarm in alarms).most_common(10),
        },
        "event_cards": cards,
        "noise_audit": build_noise_audit(alarms, assigned, clusters, dependencies, inventory),
    }


HTML = """
<!doctype html>
<html lang="tr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>CFDI Alarm Korelasyon Paneli</title>
  <style>
    :root {
      --ink: #1e2328;
      --muted: #65707a;
      --paper: #f7f2ea;
      --panel: #fffaf1;
      --line: #ded3c2;
      --danger: #c7352d;
      --warn: #d58022;
      --ok: #317a57;
      --blue: #276b9f;
      --charcoal: #29343d;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      color: var(--ink);
      background:
        linear-gradient(135deg, rgba(39,107,159,.12), transparent 32%),
        radial-gradient(circle at 85% 0%, rgba(199,53,45,.10), transparent 30%),
        repeating-linear-gradient(0deg, rgba(41,52,61,.035), rgba(41,52,61,.035) 1px, transparent 1px, transparent 28px),
        var(--paper);
      font-family: Avenir Next, Segoe UI, Helvetica Neue, sans-serif;
    }
    header {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 18px;
      align-items: end;
      padding: 22px 28px 14px;
      border-bottom: 1px solid var(--line);
      background: rgba(255,250,241,.86);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 0;
      z-index: 2;
    }
    h1 { margin: 0; font-size: clamp(24px, 4vw, 40px); letter-spacing: 0; }
    .subtitle { color: var(--muted); margin-top: 6px; max-width: 900px; }
    .toolbar { display: flex; gap: 8px; align-items: center; flex-wrap: wrap; justify-content: flex-end; }
    button, select {
      border: 1px solid var(--charcoal);
      background: #fff;
      color: var(--ink);
      min-height: 38px;
      border-radius: 6px;
      padding: 8px 10px;
      font: inherit;
    }
    button { cursor: pointer; }
    main { padding: 22px 28px 40px; }
    .metrics { display: grid; grid-template-columns: repeat(4, minmax(140px, 1fr)); gap: 12px; margin-bottom: 18px; }
    .metric, .card, .noise-panel {
      background: rgba(255,250,241,.94);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 10px 24px rgba(41,52,61,.07);
    }
    .metric { padding: 14px; min-height: 88px; }
    .metric span { display: block; color: var(--muted); font-size: 13px; }
    .metric strong { display: block; font-size: 30px; margin-top: 6px; }
    .grid { display: grid; grid-template-columns: minmax(0, 1.3fr) minmax(320px, .7fr); gap: 16px; align-items: start; }
    .cards { display: grid; gap: 12px; }
    .card { padding: 16px; border-left: 7px solid var(--warn); }
    .card.sev5 { border-left-color: var(--danger); }
    .card.sev4 { border-left-color: var(--warn); }
    .card h2 { margin: 0 0 8px; font-size: 20px; letter-spacing: 0; }
    .meta { display: flex; flex-wrap: wrap; gap: 8px; margin: 10px 0; }
    .chip { border: 1px solid var(--line); border-radius: 999px; padding: 4px 8px; background: #fff; color: var(--charcoal); font-size: 13px; }
    .chips-tight { display: flex; flex-wrap: wrap; gap: 5px; margin-top: 8px; }
    .reason { color: var(--charcoal); line-height: 1.45; }
    .evidence { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; margin-top: 12px; }
    .box { background: #fff; border: 1px solid var(--line); border-radius: 6px; padding: 10px; min-height: 80px; }
    .box h3 { margin: 0 0 6px; font-size: 13px; color: var(--muted); text-transform: uppercase; letter-spacing: 0; }
    details.group { margin-top: 12px; border: 1px solid var(--line); border-radius: 8px; background: #fff; overflow: hidden; }
    details.group summary { cursor: pointer; padding: 10px 12px; font-weight: 700; background: #f4eadb; }
    .service-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 8px; padding: 12px; }
    .service-tile { border: 1px solid var(--line); border-radius: 6px; padding: 9px; background: #fffaf1; }
    .service-tile strong { display: block; }
    .alarm-table-wrap { max-height: 360px; overflow: auto; border-top: 1px solid var(--line); }
    .alarm-table { min-width: 980px; }
    .sev-pill { display: inline-block; min-width: 24px; text-align: center; border-radius: 999px; padding: 2px 7px; color: #fff; background: var(--blue); font-weight: 700; }
    .sev-pill.s5 { background: var(--danger); }
    .sev-pill.s4 { background: var(--warn); }
    .action { display: grid; grid-template-columns: 1fr auto; gap: 10px; align-items: center; margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--line); }
    .status { font-weight: 700; color: var(--blue); }
    .noise-panel { padding: 16px; position: sticky; top: 96px; }
    .noise-panel h2 { margin-top: 0; }
    table { width: 100%; border-collapse: collapse; font-size: 13px; }
    th, td { border-bottom: 1px solid var(--line); padding: 8px 4px; text-align: left; vertical-align: top; }
    th { color: var(--muted); }
    .bar { height: 9px; background: #eadcca; border-radius: 999px; overflow: hidden; margin-top: 4px; }
    .bar span { display: block; height: 100%; background: var(--blue); }
    dialog { border: 1px solid var(--charcoal); border-radius: 8px; max-width: min(940px, 92vw); background: var(--panel); color: var(--ink); }
    dialog::backdrop { background: rgba(30,35,40,.45); }
    .hidden { display: none; }
    @media (max-width: 960px) {
      header, .grid { grid-template-columns: 1fr; }
      .metrics { grid-template-columns: repeat(2, minmax(0, 1fr)); }
      .noise-panel { position: static; }
    }
    @media (max-width: 560px) {
      main, header { padding-left: 14px; padding-right: 14px; }
      .metrics, .evidence { grid-template-columns: 1fr; }
      .action { grid-template-columns: 1fr; }
    }
  </style>
</head>
<body>
  <header>
    <div>
      <h1>CFDI Alarm Korelasyon Paneli</h1>
      <div class="subtitle" id="subtitle">Yukleniyor...</div>
    </div>
    <div class="toolbar">
      <select id="statusFilter" aria-label="Aksiyon durum filtresi">
        <option value="all">Tum aksiyonlar</option>
        <option value="acik">Acik</option>
        <option value="inceleniyor">Inceleniyor</option>
        <option value="kapandi">Kapandi</option>
      </select>
      <button id="noiseButton">Gurultu Denetimi</button>
      <button id="reloadButton">Yenile</button>
    </div>
  </header>
  <main>
    <section class="metrics" id="metrics"></section>
    <section class="grid">
      <div class="cards" id="cards"></div>
      <aside class="noise-panel">
        <h2>Operasyon Ozeti</h2>
        <div id="opsSummary"></div>
      </aside>
    </section>
  </main>
  <dialog id="noiseDialog">
    <h2>Gurultu Denetimi</h2>
    <div id="noiseContent"></div>
    <form method="dialog"><button>Kapat</button></form>
  </dialog>
  <script>
    let analysis = null;
    const actionStatuses = new Map();

    async function loadAnalysis() {
      const response = await fetch('/api/analysis');
      analysis = await response.json();
      analysis.event_cards.forEach(card => actionStatuses.set(card.action.id, card.action.status));
      render();
    }

    function metric(label, value) {
      return `<div class="metric"><span>${label}</span><strong>${value}</strong></div>`;
    }

    function renderMetrics() {
      const summary = analysis.summary;
      document.getElementById('subtitle').textContent = `${summary.time_range.start} - ${summary.time_range.end} araligindaki ${summary.total_alarms} alarm isleniyor.`;
      document.getElementById('metrics').innerHTML = [
        metric('Toplam alarm', summary.total_alarms),
        metric('Olay karti', summary.event_cards),
        metric('Indirgeme orani', `${(summary.reduction_ratio * 100).toFixed(2)}%`),
        metric('Gurultu adayi', summary.noise_count)
      ].join('');
    }

    function chips(items) {
      return `<div class="chips-tight">${items.map(item => `<span class="chip">${item}</span>`).join('')}</div>`;
    }

        function renderDependencyImpact(card) {
            const observed = [...card.dependency_impact.observed_upstream, ...card.dependency_impact.observed_downstream];
            if (!observed.length) return 'Bu kartta ek dosyadaki bagimliliklerle eslesen dogrudan etki bulunamadi.';
            return `<ul>${observed.slice(0, 8).map(item => `<li>${item.source} -> ${item.target} (${item.type}, ${item.criticality})</li>`).join('')}</ul>`;
        }

        function renderServiceGroups(card) {
            return `<div class="service-grid">${card.service_groups.map(group => `
                <div class="service-tile">
                    <strong>${group.service}</strong>
                    <span>${group.alarm_count} alarm · sev ${group.max_severity} · ${group.criticality}</span>
                    <div>${group.top_alarm_types.map(([name, count]) => `${name}=${count}`).join(', ')}</div>
                </div>`).join('')}</div>`;
        }

        function renderAlarmRows(card) {
            return `<div class="alarm-table-wrap"><table class="alarm-table"><thead><tr><th>Zaman</th><th>ID</th><th>Sev</th><th>Servis</th><th>Kritiklik</th><th>Host</th><th>Lokasyon</th><th>Tip</th><th>Hedef</th><th>Mesaj</th></tr></thead><tbody>${card.grouped_alarms.map(alarm => `
                <tr>
                    <td>${alarm.timestamp}</td>
                    <td>${alarm.alarm_id}</td>
                    <td><span class="sev-pill s${alarm.severity}">${alarm.severity}</span></td>
                    <td>${alarm.service}</td>
                    <td>${alarm.service_criticality}</td>
                    <td>${alarm.host}</td>
                    <td>${alarm.location}</td>
                    <td>${alarm.alarm_type}</td>
                    <td>${alarm.target_service || '-'}</td>
                    <td>${alarm.message}</td>
                </tr>`).join('')}</tbody></table></div>`;
        }

        function renderCard(card) {
      const status = actionStatuses.get(card.action.id) || card.action.status;
      const typeBars = card.evidence.top_alarm_types.map(([name, count]) => {
        const width = Math.max(8, Math.round(count / card.alarm_count * 100));
        return `<div>${name} (${count})<div class="bar"><span style="width:${width}%"></span></div></div>`;
      }).join('');
      return `<article class="card sev${card.max_severity}" data-status="${status}">
        <h2>${card.priority}. ${card.root_hypothesis}</h2>
        <div class="meta">
          <span class="chip">${card.id}</span>
          <span class="chip">${card.alarm_count} alarm</span>
          <span class="chip">sev ${card.max_severity}</span>
          <span class="chip">${card.time_range.start} - ${card.time_range.end}</span>
          <span class="chip">guven ${(card.confidence * 100).toFixed(0)}%</span>
        </div>
        <p class="reason">${card.explanation}</p>
        <div class="evidence">
          <div class="box"><h3>Etkilenen Servisler</h3>${chips(card.affected_services.slice(0, 14))}</div>
          <div class="box"><h3>Alarm Tip Yogunlugu</h3>${typeBars}</div>
          <div class="box"><h3>Karsi Olasiliklar</h3><ul>${card.counter_possibilities.map(item => `<li>${item}</li>`).join('')}</ul></div>
                    <div class="box"><h3>Bagimlilik Etkisi</h3>${renderDependencyImpact(card)}</div>
          <div class="box"><h3>Benzer Oruntu</h3>${card.similar_patterns.length ? `<ul>${card.similar_patterns.map(item => `<li>${item}</li>`).join('')}</ul>` : 'Bu veri paketinde onceki benzer oruntu bulunamadi.'}</div>
        </div>
                <details class="group">
                    <summary>Ayni korelasyon grubundaki ${card.alarm_count} alarmi ve servis alt gruplarini goster</summary>
                    ${renderServiceGroups(card)}
                    ${renderAlarmRows(card)}
                </details>
        <div class="action">
          <div><strong>${card.action.id}</strong> ${card.action.title}<br><span class="status">${card.action.owner} · ${status}</span></div>
          <select data-action-id="${card.action.id}" aria-label="${card.action.id} durum">
            ${['acik','inceleniyor','kapandi'].map(item => `<option value="${item}" ${item === status ? 'selected' : ''}>${item}</option>`).join('')}
          </select>
        </div>
      </article>`;
    }

    function renderCards() {
      const filter = document.getElementById('statusFilter').value;
      const cards = analysis.event_cards.filter(card => filter === 'all' || (actionStatuses.get(card.action.id) || card.action.status) === filter);
      document.getElementById('cards').innerHTML = cards.map(renderCard).join('') || '<p>Bu filtrede olay karti yok.</p>';
      document.querySelectorAll('select[data-action-id]').forEach(select => {
        select.addEventListener('change', async event => {
          const actionId = event.target.dataset.actionId;
          const status = event.target.value;
          await fetch(`/api/actions/${actionId}`, {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({status})});
          actionStatuses.set(actionId, status);
          renderCards();
          renderOpsSummary();
        });
      });
    }

    function renderOpsSummary() {
      const open = [...actionStatuses.values()].filter(status => status !== 'kapandi').length;
      const severe = analysis.event_cards.filter(card => card.max_severity >= 5).length;
      const topTypes = analysis.summary.top_alarm_types.map(([name, count]) => `<tr><td>${name}</td><td>${count}</td></tr>`).join('');
      document.getElementById('opsSummary').innerHTML = `
        <p><strong>${severe}</strong> kart sev-5 kok adayina sahip. <strong>${open}</strong> aksiyon acik veya inceleniyor.</p>
        <table><thead><tr><th>Alarm tipi</th><th>Adet</th></tr></thead><tbody>${topTypes}</tbody></table>
      `;
    }

    function renderNoise() {
      const noise = analysis.noise_audit;
      const typeRows = noise.by_type.map(([name, count]) => `<tr><td>${name}</td><td>${count}</td></tr>`).join('');
    const sampleRows = noise.samples.slice(0, 40).map(row => `<tr><td>${row.alarm_id}</td><td>${row.service}</td><td>${row.service_criticality}</td><td>${row.alarm_type}</td><td>${row.severity}</td><td>${row.reason}</td></tr>`).join('');
      document.getElementById('noiseContent').innerHTML = `
        <p>${noise.count} alarm olay karti esigini gecemedigi icin gurultu/izleme adayi olarak tutuldu.</p>
        <h3>Tip Dagilimi</h3><table><tbody>${typeRows}</tbody></table>
                <h3>Ornek Denetim Satirlari</h3><table><thead><tr><th>ID</th><th>Servis</th><th>Kritiklik</th><th>Tip</th><th>Sev</th><th>Neden elendi</th></tr></thead><tbody>${sampleRows}</tbody></table>
      `;
      document.getElementById('noiseDialog').showModal();
    }

    function render() {
      renderMetrics();
      renderCards();
      renderOpsSummary();
    }

    document.getElementById('reloadButton').addEventListener('click', loadAnalysis);
    document.getElementById('noiseButton').addEventListener('click', renderNoise);
    document.getElementById('statusFilter').addEventListener('change', renderCards);
    loadAnalysis();
  </script>
</body>
</html>
"""


class AppHandler(BaseHTTPRequestHandler):
    analysis_cache: dict[str, Any] = {}
    actions: dict[str, str] = {}
    data_path: Path = default_data_path()
    dependency_path: Path = default_dependency_path()
    inventory_path: Path = default_inventory_path()

    def log_message(self, format: str, *args: Any) -> None:
        return

    def send_json(self, payload: dict[str, Any], status: HTTPStatus = HTTPStatus.OK) -> None:
        body = json.dumps(payload, ensure_ascii=False, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self) -> None:
        path = urlparse(self.path).path
        if path == "/":
            body = HTML.encode("utf-8")
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)
            return
        if path == "/api/analysis":
            payload = analyze(self.data_path, self.dependency_path, self.inventory_path)
            for card in payload["event_cards"]:
                action_id = card["action"]["id"]
                card["action"]["status"] = self.actions.get(action_id, card["action"]["status"])
            self.analysis_cache = payload
            self.send_json(payload)
            return
        self.send_error(HTTPStatus.NOT_FOUND)

    def do_POST(self) -> None:
        path = urlparse(self.path).path
        if not path.startswith("/api/actions/"):
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        action_id = path.rsplit("/", 1)[-1]
        length = int(self.headers.get("Content-Length", "0"))
        payload = json.loads(self.rfile.read(length) or b"{}")
        status = payload.get("status")
        if status not in {"acik", "inceleniyor", "kapandi"}:
            self.send_json({"error": "Gecersiz durum"}, HTTPStatus.BAD_REQUEST)
            return
        self.actions[action_id] = status
        self.send_json({"action_id": action_id, "status": status})


def serve(data_path: Path, dependency_path: Path, inventory_path: Path, host: str, port: int) -> None:
    AppHandler.data_path = data_path
    AppHandler.dependency_path = dependency_path
    AppHandler.inventory_path = inventory_path
    server = ThreadingHTTPServer((host, port), AppHandler)
    print(f"Alarm korelasyon paneli: http://{host}:{port}")
    print(f"Veri dosyasi: {data_path}")
    print(f"Bagimlilik dosyasi: {dependency_path if dependency_path.exists() else 'bulunamadi'}")
    print(f"Envanter dosyasi: {inventory_path if inventory_path.exists() else 'bulunamadi'}")
    server.serve_forever()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="CFDI alarm korelasyon uygulamasi")
    parser.add_argument("--data", type=Path, default=default_data_path(), help="Alarm CSV yolu")
    parser.add_argument("--dependencies", type=Path, default=default_dependency_path(), help="Servis bagimlilik CSV yolu")
    parser.add_argument("--inventory", type=Path, default=default_inventory_path(), help="Host envanter CSV yolu")
    parser.add_argument("--host", default="127.0.0.1", help="Web sunucu host")
    parser.add_argument("--port", type=int, default=8000, help="Web sunucu port")
    parser.add_argument("--json", action="store_true", help="Web sunucusu baslatmadan analiz JSON'u yazdir")
    args = parser.parse_args(argv)

    try:
        if args.json:
            print(json.dumps(analyze(args.data, args.dependencies, args.inventory), ensure_ascii=False, indent=2))
        else:
            serve(args.data, args.dependencies, args.inventory, args.host, args.port)
    except (FileNotFoundError, ValueError) as exc:
        print(f"Hata: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())