# CFDI Alarm Korelasyon Paneli

CFDI ekibinin **AO Hackathon 2026 / S-A1 Alarm Fırtınası** senaryosu için geliştirdiği korelasyon uygulamasıdır.

## Proje Özeti

**Proje adı:** CFDI Alarm Korelasyon Paneli

**Tek cümlelik özet:** 3.000 satırlık alarm akışını kök neden hipotezi, kanıt, karşı olasılık ve izlenebilir aksiyon içeren 7 olay kartına indirger.

## Çözdüğümüz Problem

Senaryoda nöbetçi mühendis, iki saatlik pencerede farklı izleme sistemlerinden gelen binlerce alarmı aynı anda görüyor. Asıl zorluk alarm sayısı değil; hangi alarmın kök neden, hangisinin türev etki ve hangisinin gürültü olduğunu ayırt edememek.

Bu uygulama alarm selini okunabilir olay kartlarına indirger. Her kartta kök neden hipotezi, etkilenen servisler, alarm sayısı, zaman aralığı, önerilen ilk aksiyon, aksiyon sahibi ve durum bilgisi gösterilir.

## Çözüm Nasıl Çalışıyor?

1. `alarms.csv` dosyasının tamamı okunur ve kolon yapısı doğrulanır.
2. Alarm tipi, şiddet, zaman, servis, lokasyon ve mesaj içindeki hedef servis bilgisi çıkarılır.
3. Kök adayları skorlanır: yüksek şiddetli ağ kesintisi, paket kaybı, disk doluluğu, DB yazma hatası, bağlantı havuzu tükenmesi ve işlem hataları daha yüksek ağırlık alır.
4. Yakın zaman, aynı lokasyon, aynı servis veya hedef servis bağı bulunan alarmlar korele edilerek olay kartlarına atanır.
5. Olay kartına atanamayan alarmlar yok sayılmaz; gürültü denetimi altında neden elendiğiyle listelenir.
6. Web panelinde kartlar, açıklamalar, karşı olasılıklar ve aksiyon durumları canlı olarak görülebilir.

Detaylı mimari: [docs/mimari.md](docs/mimari.md)

## Kurulum

### Ön Koşullar

- Python 3.11+
- Harici Python paketi gerekmez.
- Resmi veri paketindeki `alarms.csv` dosyası gerekir.

Veri dosyaları için önerilen varsayılan yol:

- `data/raw/alarms.csv`
- `data/raw/service_dependencies.csv`
- `data/raw/host_inventory.csv`

Alternatif olarak aşağıdaki yol da desteklenir:

- `data/alarms.csv`
- `data/service_dependencies.csv`
- `data/host_inventory.csv`

İstenirse komutta `--data /dosya/yolu/alarms.csv` da verilebilir.

### Çalıştırma

Web paneli:

```bash
python3 src/app.py --port 8000
```

Tarayıcı adresi:

```text
http://127.0.0.1:8000
```

JSON analiz çıktısı:

```bash
python3 src/app.py --json
```

## Doğrulanan Sonuçlar

`python3 src/app.py --json` komutu çalıştırıldı.

| Metrik | Sonuç | Ölçüm / Hesaplama Yöntemi |
|---|---:|---|
| İşlenen alarm | 3.000 | CSV satır sayısı |
| Üretilen olay kartı | 7 | Korelasyon çıktısındaki `event_cards` sayısı |
| İndirgeme oranı | %0,23 (7 / 3000) | `7 / 3000` |
| Gürültü / izleme adayı | 1.755 | Olay kartına atanmayıp denetim görünümüne alınan alarmlar |
| İlk karttaki grup alarmı | 391 | İlk olay kartının `grouped_alarms` sayısı |

HTTP API ayrıca `ACT-01` aksiyonunun `acik` durumundan `inceleniyor` durumuna geçirilebildiğini doğruladı.

## AI Stratejisi ve İş Bölümü

Bu geliştirme sırasında GitHub Copilot Chat kullanıldı.

- Araç: GitHub Copilot Chat
- VS Code Copilot extension sürümü: 0.65.0
- VS Code sürümü: 1.137.0
- Oturum tarihi: 2026-09-16

| Aşama | AI'ın Rolü | İnsan Kararı / Doğrulaması |
|---|---|---|
| Senaryo analizi | Gereksinimleri çalışan bileşenlere çevirmek | Senaryo ve veri paketinin gerçek olduğunu sağlamak |
| Algoritma tasarımı | Korelasyon skoru, kök aday seçimi ve açıklama yapısını önermek | Kök neden iddialarının hipotez olarak kalması |
| Kodlama | Python uygulamasını, API'yi ve dashboard'u üretmek | Komutları çalıştırarak çıktıyı doğrulamak |
| Dokümantasyon | Gerçek ölçümlere dayalı doküman taslağı oluşturmak | Final takım bilgisi ve model sürümünü doğrulamak |

Kritik prompt kaydı: [prompts/used/2026-09-16-korelasyon-uygulamasi.md](prompts/used/2026-09-16-korelasyon-uygulamasi.md)

## Açıklanabilirlik ve X-Factor

Her olay kartı yalnızca bir başlık üretmez; kök neden hipotezini şu kanıtlarla birlikte verir:

- İlk güçlü sinyal ve zaman bilgisi
- Baskın alarm tipleri
- Etkilenen servisler
- En yoğun lokasyon
- Karşı olasılıklar
- Benzer geçmiş örüntü notu
- Gürültü olarak elenen alarmlar için denetim gerekçesi

**X-Factor:** Aynı panelde hem kök neden hipotezini hem de karşı olasılıkları ve gürültü denetimini göstermek. Bu, kartların neden üretildiğini ve hangi alarmların neden dışarıda kaldığını jüriye canlı olarak göstermeyi sağlar.

Kod kanıtı: [src/app.py](src/app.py)

## Demo

Demo akışı: [demo/README.md](demo/README.md)

Özet demo:

1. Web paneli açılır ve 3.000 alarmın 7 karta indirildiği gösterilir.
2. İlk olay kartında `dc1/rack-A` ağ problemi hipotezi, etkilenen servisler ve kanıtlar incelenir.
3. Kart içindeki açılır bölümden aynı korelasyon grubundaki alarm tablosu ve servis alt grupları gösterilir.
4. Gürültü denetimi açılır ve elenen alarm örneklerinin nedenleri gösterilir.
5. `ACT-01` aksiyonu `acik` durumundan `inceleniyor` veya `kapandi` durumuna alınır.

## Harici Bağımlılıklar, MCP ve API

- Harici Python paketi kullanılmadı.
- MCP sunucusu kullanılmadı.
- Harici API entegrasyonu kullanılmadı.
- Kalıcı veritabanı kullanılmadı; aksiyon durumu demo sırasında bellek içinde tutulur.
- Kullanılan AI çalışma ortamı: GitHub Copilot Chat + VS Code Copilot extension 0.65.0 + VS Code 1.137.0

## Bilinen Sınırlar

- Kök nedenler doğrulama verisi olmadan hipotez olarak sunulur; kesin gerçek kök nedeni garanti edilmez.
- Aksiyon durumları süreç boyunca bellekte tutulur; uygulama yeniden başlatıldığında sıfırlanır.
- Korelasyon kuralları senaryodaki CSV alanlarına göre tasarlanmıştır; farklı şema için uyarlama gerekir.
- Farklı bir Copilot model adı/sürümü raporlanacaksa bu bilgi ekip tarafından ayrıca doğrulanmalıdır.
