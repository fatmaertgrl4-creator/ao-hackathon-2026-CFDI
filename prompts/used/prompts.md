# Sohbet Prompt Kanıtları

Bu dosya, bu Copilot Chat oturumunda kullanıcı tarafından verilen ana promptları saatleriyle ve jüri tarafından anlaşılabilecek kısa yorumlarla kaydeder.

**Oturum:** `e7deaef3-97ac-42d1-a5b6-733c4e87d5bf`  
**Tarih:** 2026-09-16  
**Saat dilimi:** Türkiye saati (`UTC+03:00`)  
**Saat kaynağı:** İlk üç prompt yerel Copilot session store kayıtlarından UTC olarak alınıp `UTC+03:00` saatine çevrildi. Son prompt, oturum henüz kapanmadan kaydedildiği için sistem saatinden alındı.

## 1. İlk Uygulama İsteği

**Saat:** 14:51:41

**Prompt:**

```text
korelasyon algoritmasıyla bir uygulama yazarak ekte ki bilgilerle bir uyulama yazar mısın senaryo brifinge de ki isterelri karşılasın
```

**Jüri için kısa yorum:**

Bu prompt, çözümün başlangıç noktasıdır. Kullanıcı S-A1 Alarm Fırtınası brifingindeki zorunlu gereksinimleri karşılayan çalışan bir korelasyon uygulaması istedi. Bu istek sonucunda CSV okuyan, alarm korelasyonu yapan, olay kartı üreten, aksiyon durumu izleyen ve web paneli sunan ilk uygulama geliştirildi.

**Repository kanıtı:**

- [../../src/app.py](../../src/app.py)
- [../../README.md](../../README.md)
- [../../AI_JURI.md](../../AI_JURI.md)
- [../../docs/mimari.md](../../docs/mimari.md)

## 2. Ek Veri ve Grup Görünümü İsteği

**Saat:** 15:11:29

**Prompt:**

```text
ekte ki bilgileri de kullnarak, korele ettiğin alarmların daha kullanıcı dostu vir ekranda gösterir misin, yani aynı korelasyona ait alarmlar aynı grupta yer almalı
```

**Jüri için kısa yorum:**

Bu prompt, uygulamanın kullanıcı deneyimini ve kanıt görünürlüğünü güçlendirdi. Kullanıcı, `service_dependencies.csv` ve `host_inventory.csv` dosyalarının da kullanılmasını ve aynı korelasyona ait alarmların aynı grup altında görülebilmesini istedi. Bu istek sonucunda kartların içine servis alt grupları, alarm satır tablosu, servis/host kritiklik bilgisi ve bağımlılık etkisi eklendi.

**Repository kanıtı:**

- [../../src/app.py](../../src/app.py)
- [../../src/README.md](../../src/README.md)
- [../../demo/README.md](../../demo/README.md)
- [../../docs/mimari.md](../../docs/mimari.md)

## 3. İndirgeme Oranı ve Yanlış Birleştirme Dengesi

**Saat:** 15:14:29

**Prompt:**

```text
indirgeme oranını artırmanın bir yolu var mı ama gerekçelemeyi bozmayalım. **Başarı nasıl ölçülür******

•    İndirgeme oranı: üretilen kart sayısının toplam alarm sayısına oranı.

•    Kök neden isabeti: kapalı doğrulama dosyasındaki gerçek köklerden kaçının yakalandığı.

•    Yanlış birleştirme: birbiriyle ilgisiz iki olayın tek karta konulup konulmadığı.
```

**Jüri için kısa yorum:**

Bu prompt, çözümün değerlendirme metriklerine göre iyileştirilmesini sağladı. Kullanıcı kart sayısını azaltmak isterken gerekçelendirme ve yanlış birleştirme riskinin bozulmamasını özellikle vurguladı. Bu nedenle yalnızca aynı kategori, aynı servis/lokasyon, aynı alarm ailesi ve çakışan ya da yakın zaman penceresi koşullarını sağlayan kartları birleştiren muhafazakar konsolidasyon eklendi. Son doğrulamada 3.000 alarm 7 olay kartına indirildi.

**Repository kanıtı:**

- [../../src/app.py](../../src/app.py)
- [../../README.md](../../README.md)
- [../../submission.json](../../submission.json)
- [../../docs/plan.md](../../docs/plan.md)

## 4. Prompt Kanıtı ve GitHub'a Push İsteği

**Saat:** 15:40:06

**Prompt:**

```text
bu sohbetteki tüm promptları saatleriyle templates/used/ altına prompts.md oluşturarak jürinin anlayabileceği dilde kısa commentlerle kanıt ekle. uygulamanın son halini github reposuna pushla
```

**Jüri için kısa yorum:**

Bu prompt, AI kullanım sürecinin şeffaf şekilde belgelenmesini ve son çalışan çözümün GitHub reposuna gönderilmesini istedi. Bu dosya, ilgili isteğin doğrudan çıktısıdır. Dosya yolu takım klasör yapısına uygun olarak `prompts/used/prompts.md` altında tutuldu.

**Repository kanıtı:**

- [prompts.md](prompts.md)
- [../../submission.json](../../submission.json)

## Özet

Bu oturumdaki promptlar, çözümün dört ana gelişim aşamasını gösterir:

1. Senaryo gereksinimlerine uygun ilk korelasyon uygulaması.
2. Bağımlılık/envanter verisiyle zenginleştirilmiş grup alarm ekranı.
3. İndirgeme oranını iyileştiren, yanlış birleştirme riskini sınırlayan konsolidasyon.
4. AI kullanım kanıtlarının kaydedilmesi ve GitHub'a gönderim hazırlığı.
