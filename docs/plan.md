# Plan

## 1. Hedef

S-A1 Alarm Fırtınası senaryosunda nöbetçi mühendisin 3.000 alarmı tek tek incelemeden karar alabilmesi için alarm akışını en fazla 15 olay kartına indirgemek.

Temel çıktı: kök neden hipotezi, etkilenen servis listesi, alarm sayısı, zaman aralığı, önerilen aksiyon, sahip ve durum bilgisi içeren web paneli.

## 2. Problem Tanımı

### Problem

Alarm akışı içinde kök neden, türev etki ve gürültü birbirine karışıyor. Bu durum müdahale sırasını belirsizleştiriyor.

### Operasyon / SRE Etkisi

Nöbetçi mühendis kök nedene değil türev etkiye müdahale ederse çözüm süresi uzar. Açıklanabilir olay kartları müdahale önceliğini daha görünür hale getirir.

### Beklenen Sonuç

- Tüm veri setinin işlenmesi
- 15 veya daha az olay kartı
- Her kartta kök neden hipotezi ve kanıt
- Her kartta aksiyon, sahip ve durum
- Gürültü olarak elenen alarmların denetlenebilmesi

## 3. Kapsam

### Kapsam İçi

- CSV veri okuma
- Korelasyon algoritması
- Web paneli
- JSON API
- Aksiyon durum izleme
- Gürültü denetimi
- Aynı korelasyon grubundaki alarm satırlarını kart içinde gösterme
- Servis bağımlılığı ve host envanteriyle zenginleştirme
- Açıklanabilir kart üretimi

### Kapsam Dışı

- Gerçek zamanlı akış altyapısı
- Kullanıcı girişi ve yetkilendirme
- Kalıcı veritabanı
- Harici AI API entegrasyonu

## 4. Başarı Kriterleri

| Kriter | Hedef | Ölçüm / Doğrulama Yöntemi | Durum |
|---|---|---|---|
| Tüm alarm akışı işlenir | 3.000 satır | JSON çıktısı `summary.total_alarms` | Tamamlandı |
| Kart sayısı | En fazla 15 | JSON çıktısı `summary.event_cards` | Tamamlandı: 7 |
| Aksiyon izleme | En az bir aksiyon durumu değişir | HTTP POST ve tekrar okuma | Tamamlandı |
| Açıklanabilirlik | Her kartta gerekçe ve karşı olasılık | API alanları ve web paneli | Tamamlandı |
| Gürültü denetimi | Elenen alarmlar nedenli listelenir | `noise_audit.samples` | Tamamlandı |

## 5. İlk Analiz ve Hipotezler

### Veri Hakkında Gözlemler

- Veri setinde 3.000 alarm var.
- Zaman aralığı `2026-09-10T01:30:20` ile `2026-09-10T03:30:20` arasında.
- Kritik alarmlar özellikle `dc1/rack-A` çevresinde yoğunlaşıyor.
- DB ve işlem hataları ayrı dalgalar oluşturuyor.

### Hipotezler

1. Aynı lokasyon ve yakın zaman içindeki ağ alarmları tek kök olay olarak gruplanabilir.
2. `disk_full`, `db_write_fail` ve `db_conn_pool` tipleri veritabanı kapasite/yazma sorununa işaret eder.
3. `timeout`, `conn_refused`, `http_5xx`, `txn_fail` ve `thread_pool` alarmları çoğunlukla türev servis etkisi veya servis olayıdır.
4. Düşük şiddetli bakım/kaynak uyarıları güçlü bağ kurmuyorsa gürültü denetimine alınmalıdır.

## 6. Seçilen Yaklaşım

**Karar:** Kural tabanlı, açıklanabilir korelasyon algoritması.

**Neden:** Senaryo hızlı demo ve gerekçeli karar istiyor. Deterministik skorlar her kartın neden oluştuğunu açıklamayı kolaylaştırıyor ve harici bağımlılık gerektirmiyor.

**Dayandığı kanıt:** İlk veri kontrolünde 3.000 satır, kritik alarm tipleri ve lokasyon yoğunlaşması gözlendi. Uygulama aynı veriyle 7 kart üretti.

## 7. AI Stratejisi

GitHub Copilot Chat geliştirme sırasında kullanıldı. Ürün içinde canlı LLM çağrısı yoktur.

AI'ın rolü:

- Senaryo gereksinimlerini bileşenlere ayırmak
- Korelasyon algoritması taslağı oluşturmak
- Python uygulaması ve web paneli kodunu üretmek
- Dokümantasyon taslağını gerçek ölçümlerle güncellemek

İnsan kontrolünde kalan kararlar:

- Kök nedenlerin hipotez olarak sunulması
- Doğrulama komutlarının çalıştırılması
- Final takım ve model bilgilerinin doğrulanması

## 8. Doğrulama Sonuçları

Çalıştırılan komut:

```bash
python3 src/app.py --json
```

Sonuç:

- Toplam alarm: 3.000
- Olay kartı: 7
- İndirgeme oranı: 0,00233
- Gürültü / izleme adayı: 1.755
- İlk karttaki grup alarmı: 391
- İlk karttaki servis alt grubu: 13

HTTP doğrulaması:

- `GET /api/analysis` 3.000 alarm ve 7 kart döndürdü.
- `POST /api/actions/ACT-01` ile aksiyon durumu `inceleniyor` yapıldı ve tekrar okundu.
