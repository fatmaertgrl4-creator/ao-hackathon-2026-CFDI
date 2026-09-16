# Mimari

## 1. Genel Mimari

CFDI Alarm Korelasyon Paneli tek Python giriş noktasıyla çalışan, harici paket gerektirmeyen bir uygulamadır. Uygulama `alarms.csv` dosyasını toplu okur, alarmları kök adaylarına göre korele eder, olay kartları üretir ve sonuçları hem JSON API hem de web paneli üzerinden sunar.

```text
[ alarms.csv + service_dependencies.csv + host_inventory.csv ]
      |
      v
[ CSV okuma ve doğrulama ]
      |
      v
[ Alarm zenginleştirme ]
  - zaman
  - şiddet
  - servis
  - lokasyon
  - hedef servis
  - servis bağımlılığı
  - host / servis kritiklik bilgisi
      |
      v
[ Kök aday skoru ]
      |
      v
[ Korelasyon ve alarm atama ]
      |
      +--> [ Olay kartları ]
      |
      +--> [ Gürültü denetimi ]
      |
      v
[ JSON API + Web paneli ]
```

## 2. Veri ve Karar Akışı

1. `load_alarms` CSV dosyasını tamamen okur ve zorunlu kolonları doğrular.
2. `parse_target_service` mesaj metninden hedef servisleri çıkarır. Örneğin `billing-service servisine yapılan çağrı zaman aşımına uğradı` gibi mesajlar bağımlılık ilişkisi olarak kullanılır.
3. `classify_alarm` alarmı ağ, veritabanı, servis, runtime veya kaynak sınıfına ayırır.
4. `root_score` yüksek şiddetli ve kök neden olma ihtimali yüksek alarm tiplerini öne çıkarır.
5. `seed_clusters` en güçlü kök adaylarından en fazla 15 olay tohumu seçer.
6. `correlation_score` her alarmın olay kartına yakınlığını zaman, servis, lokasyon, hedef servis ve servis bağımlılık bağıyla hesaplar.
7. `assign_alarms` eşiği geçen alarmları kartlara atar.
8. `consolidate_related_clusters` aynı kategori, aynı locus, aynı alarm ailesi ve çakışan/yakın pencere koşulunu sağlayan tekrar kartlarını birleştirir.
9. `build_noise_audit` kartlara girmeyen alarmları nedenleriyle denetim listesine alır.
10. `AppHandler` JSON API ve web panelini sunar.

## 3. Bileşenler

| Bileşen | Kod Konumu | Girdi | Çıktı | Doğrulama |
|---|---|---|---|---|
| CSV okuyucu | [src/app.py](../src/app.py) | `alarms.csv` | Sıralı alarm nesneleri | 3.000 satır okundu |
| Ek veri okuyucu | [src/app.py](../src/app.py#L140-L177) | Bağımlılık ve envanter CSV'leri | Servis grafiği, host/servis kritikliği | API çıktısında ek veri yolları doğrulandı |
| Kök aday seçimi | [src/app.py](../src/app.py#L277-L303) | Zenginleştirilmiş alarmlar | Olay tohumları | En fazla 15 aday sınırı korundu |
| Korelasyon skoru | [src/app.py](../src/app.py#L306-L360) | Alarm + olay tohumu + bağımlılık grafiği | Skor | JSON çıktısı üretildi |
| Alarm atama | [src/app.py](../src/app.py#L362-L371) | Tüm alarmlar + kartlar | Atanmış alarm kümesi | Olay ve gürültü toplamı 3.000 alarmı kapsıyor |
| Tekrar kart konsolidasyonu | [src/app.py](../src/app.py#L376-L421) | Aynı kök ailesindeki tekrar kartları | Daha az ama gerekçeli kart | 15 kart 7 karta indirildi |
| Olay kartı | [src/app.py](../src/app.py#L545-L601) | Korele alarm grubu | Kök hipotezi, servis listesi, grup alarm tablosu, zaman aralığı, aksiyon | API çıktısı doğrulandı |
| Gürültü denetimi | [src/app.py](../src/app.py#L604-L625) | Atanmayan alarmlar | Nedenli denetim listesi | 1.755 gürültü adayı listelendi |
| Web/API | [src/app.py](../src/app.py#L663-L1019) | HTTP istekleri | Dashboard, grup alarm görünümü, analiz API, aksiyon API | `curl` ile doğrulandı |

## 4. AI / LLM Entegrasyonu

Çalışan ürün içinde canlı LLM veya harici AI API çağrısı yoktur. AI bu geliştirme sürecinde GitHub Copilot Chat olarak kullanıldı: senaryo gereksinimlerinin çözüme çevrilmesi, algoritma tasarımı, kod üretimi ve dokümantasyon taslağı için destek verdi.

Model çıktıları doğrudan gerçek kabul edilmedi; uygulama `python3 src/app.py --data /Users/TCNGUNDUZ/Downloads/katilimci_paketi/alarms.csv --dependencies /Users/TCNGUNDUZ/Downloads/katilimci_paketi/service_dependencies.csv --inventory /Users/TCNGUNDUZ/Downloads/katilimci_paketi/host_inventory.csv --json` ve HTTP API kontrolleriyle doğrulandı.

## 5. Açıklanabilirlik / XAI Akışı

Her olay kartı şu yapıda üretilir:

```text
KÖK NEDEN HİPOTEZİ
  +
GEREKÇE
  +
KANIT
  +
KARŞI OLASILIKLAR
  +
AKSİYON
```

Bu yaklaşımda korelasyon nedensellik olarak kesinleştirilmez. Kart başlıkları hipotezdir; kanıt bölümünde baskın alarm tipleri, alarm sayısı, etkilenen servisler, lokasyon ve örnek alarm ID'leri gösterilir.

## 6. Harici Bağımlılıklar

Harici paket, MCP sunucusu, harici API veya kalıcı veritabanı kullanılmadı. Uygulama Python standart kütüphanesiyle çalışır.

## 7. Bilinen Mimari Sınırlar

- Aksiyon durumları bellek içinde tutulur; sunucu yeniden başlatılırsa sıfırlanır.
- Korelasyon kuralları verilen CSV şemasına göre ayarlanmıştır.
- Kök neden doğruluğu doğrulama etiketi olmadan ölçülemez; çıktı hipotez olarak sunulur.
