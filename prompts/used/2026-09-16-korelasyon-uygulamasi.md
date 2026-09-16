# Korelasyon Uygulaması Geliştirme Prompt Kaydı

## Amaç

S-A1 Alarm Fırtınası senaryosundaki zorunlu gereksinimleri karşılayan çalışan bir korelasyon uygulaması geliştirmek.

## Araç / Model

- Araç: GitHub Copilot Chat
- Model: GitHub Copilot
- Sürüm: Bu oturumda doğrulanmadı
- Tarih: 2026-09-16

## Bağlam

Kullanıcı senaryo brifingini ve `alarms.csv` / `alarms.json` veri paketini ekledi. Senaryo, 3.000 alarmın en fazla 15 olay kartına indirilmesini, her kartta kök neden hipotezi, etkilenen servisler, alarm sayısı, zaman aralığı ve aksiyon bilgisi gösterilmesini istiyordu.

## Gerçek Prompt

```text
korelasyon algoritmasıyla bir uygulama yazarak ekte ki bilgilerle bir uyulama yazar mısın senaryo brifinge de ki isterelri karşılasın
```

## Önemli Çıktı Özeti

- `src/app.py` içinde Python standart kütüphanesiyle çalışan korelasyon uygulaması yazıldı.
- Web paneli, JSON analiz API'si ve aksiyon durum API'si eklendi.
- 3.000 alarmın 7 olay kartına indirildiği doğrulandı.
- `service_dependencies.csv` ve `host_inventory.csv` kullanılarak bağımlılık etkisi, servis kritiklikleri ve grup alarm tablosu eklendi.
- Gürültü denetimi ve karşı olasılık açıklamaları eklendi.

## İnsan Kararı / Doğrulama

Aşağıdaki komutlar çalıştırılarak çıktı doğrulandı:

```bash
python3 src/app.py --json
curl -s http://127.0.0.1:8000/api/analysis
curl -s -X POST http://127.0.0.1:8000/api/actions/ACT-01 -H 'Content-Type: application/json' -d '{"status":"inceleniyor"}'
```

## Repository Kanıtı

- [../../src/app.py](../../src/app.py)
- [../../README.md](../../README.md)
- [../../AI_JURI.md](../../AI_JURI.md)
- [../../docs/mimari.md](../../docs/mimari.md)
