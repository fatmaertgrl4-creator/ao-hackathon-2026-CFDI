# AI Jüri Özeti

**Takım:** CFDI  
**Repo:** https://github.com/fatmaertgrl4-creator/ao-hackathon-2026-CFDI

## 1. AI Stratejimiz ve İş Akışı

### Kullandığımız AI Araçları

| Araç / Platform | Model | Sürüm | Kullanım Amacı |
|---|---|---|---|
| GitHub Copilot Chat | GitHub Copilot Chat | VS Code Copilot extension 0.65.0 · VS Code 1.137.0 · Oturum: 2026-09-16 | Senaryo analizi, algoritma taslağı, kod geliştirme ve dokümantasyon desteği |

SAKA bu uygulama geliştirme adımında çalışan ürün içine entegre edilmedi. Final teslimde SAKA kullanılırsa model adı ve sürümü ayrıca doğrulanmalıdır.

### AI'ı Nasıl Kullandık?

AI, senaryo gereksinimlerini uygulanabilir bileşenlere çevirmek, korelasyon yaklaşımını şekillendirmek, Python uygulamasını üretmek ve dokümantasyonu gerçek doğrulama çıktılarıyla güncellemek için kullanıldı.

Ürün içinde canlı LLM çağrısı yoktur; nihai olay kartları deterministik korelasyon algoritmasıyla üretilir.

Claude tabanlı kullanım için hazırlanan `skills/` ve `prompts/templates/` yapıları, geliştirme sürecinde Copilot tercih edildiği için kullanılmamış ve başlangıç repo bütünlüğünü korumak amacıyla değiştirilmemiştir.

### İnsan – AI İş Bölümü

| Aşama | AI'ın Rolü | İnsan Kararı / Doğrulaması |
|---|---|---|
| Problem analizi | Zorunlu ve bonus gereksinimleri bileşenlere ayırmak | Senaryonun gerçek hedefini onaylamak |
| Veri keşfi | İncelenecek sinyalleri önermek | 3.000 satır, alarm tipleri ve kritik lokasyon yoğunluğunu komutla doğrulamak |
| Kodlama | Korelasyon uygulamasını ve web panelini üretmek | Komutları çalıştırıp çıktıyı kontrol etmek |
| Test | JSON ve HTTP doğrulama komutlarını çalıştırmak | 7 kart ve aksiyon durum değişikliğini doğrulamak |
| Dokümantasyon | Gerçek metriklerle doküman taslağı oluşturmak | Takım bilgisi, iletişim ve kullanılan araç sürümlerini doğrulamak |

### İş Akışımız

Senaryo okundu, veri formatı incelendi, kök aday skoru ve korelasyon eşiği seçildi, küçük bir Python uygulaması geliştirildi, JSON ve HTTP çıktıları doğrulandı, ardından dokümantasyon gerçek ölçümlerle güncellendi.

### Kanıt

- [src/app.py](src/app.py)
- [docs/plan.md](docs/plan.md)
- [docs/mimari.md](docs/mimari.md)
- [prompts/used/2026-09-16-korelasyon-uygulamasi.md](prompts/used/2026-09-16-korelasyon-uygulamasi.md)

## 2. Problemi Nasıl Çözdük

### Problem ve Yaklaşım

S-A1 senaryosunda alarm sayısından çok alarm ilişkileri görünmez durumdaydı. Çözüm, tüm alarm akışını okuyup kök neden hipotezi etrafında gruplanmış olay kartları üretir.

Seçilen yaklaşım kural tabanlı ve açıklanabilir korelasyondur. Kök adayları alarm tipi, şiddet, yerel yoğunluk ve zaman sırasına göre skorlanır. Diğer alarmlar servis, lokasyon, zaman ve hedef servis bağına göre kartlara atanır.

### Çalışan Çözüm

Uygulama `src/app.py` üzerinden çalışır. Aynı giriş noktası hem JSON analiz hem de web paneli sunar.

Her olay kartında şu alanlar bulunur:

- Kök neden hipotezi
- Etkilenen servisler
- Alarm sayısı
- Zaman aralığı
- Açıklama ve kanıt
- Karşı olasılıklar
- Önerilen aksiyon
- Aksiyon sahibi ve durum

Kartlara atanamayan alarmlar `noise_audit` altında nedenleriyle listelenir.

### Ölçtüğümüz Sonuçlar

| Metrik | Sonuç | Ölçüm / Hesaplama Yöntemi |
|---|---:|---|
| İşlenen alarm | 3.000 | CSV satır sayısı |
| Olay kartı | 7 | `summary.event_cards` |
| İndirgeme oranı | %0,23 (7 / 3000) | `7 / 3000` |
| Gürültü / izleme adayı | 1.755 | `summary.noise_count` |
| İlk karttaki grup alarmı | 391 | İlk olay kartındaki `grouped_alarms` sayısı |
| Aksiyon durum doğrulaması | Başarılı | `ACT-01` durumu HTTP API ile `inceleniyor` yapıldı |

### Kanıt

- Ek veri okuma: [src/app.py](src/app.py#L140-L177)
- Korelasyon çekirdeği: [src/app.py](src/app.py#L277-L371)
- Grup alarm ve açıklama üretimi: [src/app.py](src/app.py#L508-L601)
- Gürültü denetimi: [src/app.py](src/app.py#L604-L625)
- Web/API: [src/app.py](src/app.py#L663-L1019)

## 3. X-Factor

### X-Factor'ımız

Açıklanabilir korelasyon ve gürültü denetimini aynı operasyon panelinde birleştirmek. Kart sadece sonuç vermez; neden bu kökün seçildiğini, hangi karşı olasılıkların bulunduğunu ve hangi alarmların neden dışarıda kaldığını gösterir.

Kart içinde aynı korelasyon grubundaki alarm satırları servis alt gruplarıyla birlikte açılır bölümde gösterilir. `service_dependencies.csv` bağımlılık etkisini, `host_inventory.csv` servis ve host kritikliğini zenginleştirir.

### Neden Değer Katıyor?

Nöbetçi mühendis, tek bir kart başlığına güvenmek zorunda kalmaz. Kanıt ve karşı olasılıkları aynı ekranda görerek ilk müdahale adımını daha kontrollü seçebilir. Gürültü denetimi, elenen alarmların görünmez hale gelmesini engeller.

### Kod Kanıtı

```text
src/app.py:140-177
src/app.py:277-371
src/app.py:508-625
src/app.py:663-1019
```

### Çıktı / Demo Kanıtı

```text
python3 src/app.py --json
GET http://127.0.0.1:8000/api/analysis
POST http://127.0.0.1:8000/api/actions/ACT-01
```

## 4. Çalıştırma

### Ön Koşullar

- Python 3.11+
- Resmi veri paketindeki `alarms.csv`
- Harici paket gerekmez

### Tek Komut

```bash
python3 src/app.py --port 8000
```

### Beklenen Çıktı

Terminalde aşağıdaki adres görünür:

```text
Alarm korelasyon paneli: http://127.0.0.1:8000
```

Tarayıcıda 3.000 alarm, 7 olay kartı, gürültü denetimi ve aksiyon durum kontrolleri görünür.

## 5. Bilinen Sınırlar

- Kök nedenler doğrulama etiketi olmadığı için hipotez olarak sunulur.
- Aksiyon durumları kalıcı değildir; sunucu yeniden başlatıldığında sıfırlanır.
- Çalışan üründe canlı LLM entegrasyonu yoktur.
- Farklı bir Copilot model adı veya ek araç sürümü raporlanacaksa ekip tarafından ayrıca doğrulanmalıdır.
