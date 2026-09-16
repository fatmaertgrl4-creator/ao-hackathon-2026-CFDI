# Demo

## 1. Demo Amacı

Jüriye 3.000 alarmın çalışan uygulama tarafından 7 olay kartına indirildiğini, her kartın gerekçeli kök neden hipotezi ürettiğini ve aksiyonların durum bilgisiyle izlenebildiğini göstermek.

## 2. Demo Akışı

### Adım 1 — Uygulamayı Başlat

**Amaç:** Çözümün verilen veriyle sıfırdan ayağa kalktığını göstermek.

**Komut:**

```bash
python3 src/app.py --port 8000
```

**Gösterilecek:** `http://127.0.0.1:8000` adresindeki panel.

**Kanıtlanan özellik:** Uygulama resmi veri dosyasını okuyarak sonuç üretiyor.

### Adım 2 — Olay Kartlarını İncele

**Amaç:** Alarm selinin karar verilebilir kartlara indiğini göstermek.

**Gösterilecek:** Üst metriklerde 3.000 alarm, 7 olay kartı ve %0,23 (7 / 3000) indirgeme oranı.

**Anlatılacak:** İlk kart `dc1/rack-A` ağ problemi hipotezini, etkilenen servisleri, baskın alarm tiplerini ve karşı olasılıkları gösterir.

**Kanıtlanan özellik:** Zorunlu olay kartı alanları ve XAI açıklaması.

### Adım 3 — Korelasyon Grubundaki Alarm Satırlarını Aç

**Amaç:** Aynı korelasyona ait alarmların aynı grup içinde yer aldığını göstermek.

**Gösterilecek:** Olay kartındaki açılır bölümde servis alt grupları, kritikliği ve tüm alarm satırları.

**Anlatılacak:** `service_dependencies.csv` bağımlılık etkisini, `host_inventory.csv` servis/host kritikliği bilgisini zenginleştirir.

**Kanıtlanan özellik:** Grup bazlı kullanıcı dostu alarm inceleme ekranı.

### Adım 4 — Gürültü Denetimini Aç

**Amaç:** Kart dışı kalan alarmların kaybolmadığını göstermek.

**Gösterilecek:** `Gurultu Denetimi` düğmesiyle açılan tabloda alarm ID, servis, tip, şiddet ve elenme nedeni.

**Kanıtlanan özellik:** Bonus gürültü denetimi görünümü.

### Adım 5 — Aksiyon Durumunu Değiştir

**Amaç:** Aksiyonun açıldıktan sonra izlenebildiğini göstermek.

**Gösterilecek:** `ACT-01` aksiyon durumunu `acik` değerinden `inceleniyor` veya `kapandi` değerine almak.

**Kanıtlanan özellik:** Opsiyonel aksiyon takip gereksinimi.

## 3. API ile Hızlı Doğrulama

Analiz:

```bash
curl -s http://127.0.0.1:8000/api/analysis
```

Aksiyon durumu değiştirme:

```bash
curl -s -X POST http://127.0.0.1:8000/api/actions/ACT-01 \
  -H 'Content-Type: application/json' \
  -d '{"status":"inceleniyor"}'
```

## 4. Ekran Görüntüleri

Bu çalışma sırasında gerçek çalışan panelden aşağıdaki ekran görüntüleri kaydedildi:

1. `01-dashboard.png`
2. `02-event-detail.png`
3. `03-correlation-group.png`
4. `04-noise-audit.png`
5. `05-action-status.png`
