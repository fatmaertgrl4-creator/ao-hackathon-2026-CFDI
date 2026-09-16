# src/

Bu dizin S-A1 Alarm Fırtınası çözümünün kaynak kodunu içerir.

## Kaynak Kod Yapısı

```text
src/
├── README.md
└── app.py
```

## Giriş Noktası

Ana giriş noktası: [app.py](app.py)

Web paneli:

```bash
python3 src/app.py --port 8000
```

JSON analiz:

```bash
python3 src/app.py --json
```

## Ana Bileşenler

| Bileşen | Kod Konumu | Sorumluluk | Doğrulama |
|---|---|---|---|
| Veri okuma | [app.py](app.py) | CSV'nin tamamını okumak, kolonları doğrulamak, hedef servis bilgisini çıkarmak | JSON çalıştırma komutu 3.000 satır okudu |
| Korelasyon | [app.py](app.py) | Kök adaylarını servis bağımlılığı, zaman, lokasyon ve hedef servis ilişkisiyle skorlamak | 3.000 alarm 7 karta indirildi |
| Grup alarm görünümü | [app.py](app.py) | Aynı korelasyona ait alarm satırlarını kart içinde servis alt gruplarıyla göstermek | İlk kartta 391 alarm ve 13 servis alt grubu doğrulandı |
| Açıklanabilirlik | [app.py](app.py) | Gerekçe, kanıt, karşı olasılık ve benzer örüntü üretmek | API çıktısında her kartta açıklama alanları var |
| Gürültü denetimi | [app.py](app.py) | Kart dışı kalan alarmları nedenle listelemek | `noise_audit` çıktısı üretildi |
| Web demo | [app.py](app.py) | Kartları ve aksiyon durumlarını tarayıcıda göstermek | `http://127.0.0.1:8000/api/analysis` doğrulandı |

## Bağımlılıklar

Harici paket bağımlılığı bulunmamaktadır. Python standart kütüphanesi kullanılır.

## Kod Kanıtı

- Ek veri okuma: [app.py](app.py#L140-L177)
- Kök aday seçimi: [app.py](app.py#L277-L303)
- Korelasyon skoru: [app.py](app.py#L306-L360)
- Alarm atama: [app.py](app.py#L362-L371)
- Tekrar kart konsolidasyonu: [app.py](app.py#L376-L421)
- Servis alt grupları: [app.py](app.py#L508-L526)
- Olay kartı üretimi: [app.py](app.py#L545-L601)
- Gürültü denetimi: [app.py](app.py#L604-L625)
- Web/API: [app.py](app.py#L663-L1019)
