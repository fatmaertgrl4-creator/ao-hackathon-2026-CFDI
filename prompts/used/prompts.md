# Sohbet Prompt Kanıtları

Bu dosya, bu Copilot Chat oturumunda kullanıcı tarafından verilen ana promptları saatleriyle ve jüri tarafından anlaşılabilecek kısa yorumlarla kaydeder.

**Oturum:** `e7deaef3-97ac-42d1-a5b6-733c4e87d5bf`  
**Tarih:** 2026-09-16  
**Saat dilimi:** Türkiye saati (`UTC+03:00`)  
**Saat kaynağı:** İlk üç prompt yerel Copilot session store kayıtlarından UTC olarak alınıp `UTC+03:00` saatine çevrildi. Son prompt, oturum henüz kapanmadan kaydedildiği için sistem saatinden alındı.
**Araç:** GitHub Copilot Chat  
**VS Code Copilot extension sürümü:** 0.65.0  
**VS Code sürümü:** 1.137.0

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

## 5. Submission JSON, Sürüm Bilgisi ve Git Push İsteği

**Saat:** 16:11:59

**Prompt:**

```text
`submission.json`** henüz final değil.** JSON sözdizimini ayrıca parse ettim; **geçerli JSON** ✅. Yani organizatörün bugün özellikle uyardığı “eksik virgül/bozuk JSON” problemi yok. Fakat içeride takım üyesi ve iletişim hâlâ `"Ekip tarafindan final oncesi doldurulacak"` yazıyor. Model sürümü de `"Bu oturumda dogrulanmadi"`. Bunlar finalden önce kesin doldurulmalı. buna göre submission json'ı güncelle, bu promptu da prompts/used altındaki prompts.md içerisine yaz ve githuba commitle ardından da pushla kullanılan model ve sürüm: Araç: GitHub Copilot Chat
VS Code Copilot extension sürümü: 0.65.0
VS Code sürümü: 1.137.0
Oturum tarihi: 2026-09-16 bu sürüm bilgilerini `README.md`, `AI_JURI.md` bu dosyalara da ekle ve commitleyip pushla
```

**Jüri için kısa yorum:**

Bu prompt, teslimat metadatasındaki eksik alanların kapatılmasını istedi. Kullanıcı önce `submission.json` dosyasının sözdizimsel olarak geçerli olduğunu doğruladı, ardından takım üyeleri, iletişim bilgileri ve kullanılan GitHub Copilot Chat / VS Code sürüm bilgilerinin teslim dokümanlarına işlenmesini talep etti. Bu adım sonunda `submission.json`, `README.md`, `AI_JURI.md` ve bu prompt kaydı güncellendi; değişiklikler commit edilip GitHub'a gönderildi.

**Repository kanıtı:**

- [../../submission.json](../../submission.json)
- [../../README.md](../../README.md)
- [../../AI_JURI.md](../../AI_JURI.md)
- [prompts.md](prompts.md)

## 6. Fazlar, İndirgeme Oranı ve UI Metin Güncellemesi

**Saat:** 16:26:58

**Prompt:**

```text
docs/fazlar.md dosyasını mevcut final repository durumuyla karşılaştır.

Yalnız gerçekten tamamlandığını repository üzerinden doğrulayabildiğin
maddeleri [x] yap.

Gerçekten tamamlanmamış maddeleri işaretleme.
Eski hazırlık durumlarını final proje durumu gibi bırakma.

Faz 3 ve Faz 4 durumlarını da gerçek mevcut duruma göre güncelle.

Başka hiçbir dosyaya dokunma. src/app.py içinde mevcut confidence hesaplamasını değiştirme.

Yalnız kullanıcı arayüzündeki "güven %..." ifadesini,
istatistiksel olasılık izlenimi vermeyecek şekilde
"heuristik kanıt skoru .../100" olarak değiştir.

Mevcut hesaplama, API ve korelasyon davranışını bozma.

Sonra gerçek syntax testi çalıştır. README.md, AI_JURI.md ve submission.json içindeki indirgeme oranı
ifadelerini karşılaştır.

Hesaplamayı değiştirme:
7 / 3000 = 0.00233 = yaklaşık %0.23.

İnsan tarafından okunan metinlerde bunu
"%0,23 (7 / 3000)" şeklinde anlaşılır hale getir.

submission.json içinde sayısal değer gerekiyorsa geçerli numeric JSON
değerini koru.

Başka metriği değiştirme. bu değişiklikleri yaparken prompts.mdye bu promptu yaz ve commitle ve githuba pushla
```

**Jüri için kısa yorum:**

Bu prompt, final repo durumuyla faz takibinin gerçekten hizalanmasını istedi. Kullanıcı yalnızca repository üzerinden doğrulanabilen checklist maddelerinin işaretlenmesini, faz durumlarının mevcut gerçeğe göre güncellenmesini, UI'daki güven ifadesinin istatistiksel olasılık izlenimi vermeyecek şekilde yeniden adlandırılmasını ve indirgeme oranı metninin insan tarafından daha anlaşılır hale getirilmesini talep etti. İstenen kapsam dışında korelasyon hesabına veya API davranışına dokunulmadı.

**Repository kanıtı:**

- [../../docs/fazlar.md](../../docs/fazlar.md)
- [../../src/app.py](../../src/app.py)
- [../../README.md](../../README.md)
- [../../AI_JURI.md](../../AI_JURI.md)
- [../../submission.json](../../submission.json)
- [prompts.md](prompts.md)

## 7. Kullanılmayan Claude Yapıları Notu

**Saat:** 16:40:34

**Prompt:**

```text
Claude tabanlı kullanım için hazırlanan `skills/` ve `prompts/templates/` yapıları, geliştirme sürecinde Copilot tercih edildiği için kullanılmamış ve başlangıç repo bütünlüğünü korumak amacıyla değiştirilmemiştir. bu bilgilendirmeyi ai_juri.md içerisine ekle ve commitleyip promptslara bu promptu ekle ve pushla
```

**Jüri için kısa yorum:**

Bu prompt, repoda bulunan fakat bu geliştirme sürecinde aktif kullanılmayan hazırlık yapılarının yanlış yorumlanmasını önlemek için açıklayıcı bir not eklenmesini istedi. Buna göre Claude odaklı `skills/` ve `prompts/templates/` klasörlerinin Copilot tercih edildiği için kullanılmadığı, ayrıca başlangıç repo bütünlüğünü korumak amacıyla değiştirilmediği [AI_JURI.md](../../AI_JURI.md) içine açıkça işlendi ve bu istek prompt kanıtlarına eklendi.

**Repository kanıtı:**

- [../../AI_JURI.md](../../AI_JURI.md)
- [prompts.md](prompts.md)

## 8. Demo ve Final Repo Temizliği

**Saat:** 16:44:04

**Prompt:**

```text
1. `demo/README.md`** kesin düzelmeli.** Şu an dosyada “Bu çalışma sırasında ekran görüntüsü üretilmedi” yazıyor ama `demo/` altında 5 tane gerçek ekran görüntüsü mevcut. Bu doğrudan çelişki.
2. **Veri yolu anlatımını tekleştirin.** `submission.json` varsayılan yolu `data/raw/alarms.csv` olarak veriyor. Kod da önce `data/raw/alarms.csv`, sonra `data/alarms.csv` arıyor; yani teknik olarak ikisini destekliyor. README ise ağırlıklı olarak `data/alarms.csv` anlatıyor. Hata değil ama jüri için gereksiz belirsizlik. README'ye “önerilen yol `data/raw/...`; alternatif olarak `data/...` da desteklenir” yazın.
3. `docs/fazlar.md`** final durumuna getirilmeli.** Şu anda hâlâ `Faz 3 — devam ediyor`, `Faz 4 — devam ediyor`; ayrıca “repo public”, “demo uçtan uca test edildi”, “final commit”, “final push” gibi maddeler boş. Repo public olduğunu ben doğruladım; ekran görüntülerinin de eklendiği zaten görülüyor. Finalden önce gerçek olan maddeleri işaretleyin, olmayanları zorla tamamlamayın.
4. **Gereksiz test dosyasını değerlendirin.** Root'ta hâlâ `ElifTest.txt` var. Jüri açısından faydası yoksa final repoda bırakmazdım. Daha önceki commit geçmişinde test amacı zaten iz bırakmış durumda; final görünümünün temiz olması daha iyi.
5. **Demo kanıtlarını isimlendirin.** Şu an isimler `CFDI Alarm Korelasyon.png`, `_Action`, `_Noise`, `_Statu`, `_sub` şeklinde. Çalışıyor ama jüri için `01-dashboard.png`, `02-event-detail.png`, `03-correlation-group.png`, `04-noise-audit.png`, `05-action-status.png` gibi sıralı isimler çok daha profesyonel olur. bu değişiklikleri de yap ama asla ana kodu app.py'ı data'yı vs değiştirme buradaki reponun en son halini diğer dosyalarda koru. bu promptu prompts.md içerisine ekle ve githuba commit edip pushla
```

**Jüri için kısa yorum:**

Bu prompt, final repo görünümündeki dokümantasyon ve demo çelişkilerinin temizlenmesini istedi. Kullanıcı özellikle ekran görüntüsü kanıtı ile `demo/README.md` arasındaki çelişkinin giderilmesini, veri yolu anlatımının jüri için netleştirilmesini, `docs/fazlar.md` içindeki yalnızca gerçekten doğrulanabilen final maddelerinin işaretlenmesini, gereksiz test dosyasının değerlendirilmesini ve demo ekran görüntülerinin daha profesyonel adlarla yeniden düzenlenmesini talep etti. Ana uygulama koduna ve veri dosyalarına dokunulmadan repo temizliği hedeflendi.

**Repository kanıtı:**

- [../../demo/README.md](../../demo/README.md)
- [../../README.md](../../README.md)
- [../../docs/fazlar.md](../../docs/fazlar.md)
- [prompts.md](prompts.md)

## Özet

Bu oturumdaki promptlar, çözümün sekiz ana gelişim aşamasını gösterir:

1. Senaryo gereksinimlerine uygun ilk korelasyon uygulaması.
2. Bağımlılık/envanter verisiyle zenginleştirilmiş grup alarm ekranı.
3. İndirgeme oranını iyileştiren, yanlış birleştirme riskini sınırlayan konsolidasyon.
4. AI kullanım kanıtlarının kaydedilmesi ve GitHub'a gönderim hazırlığı.
5. Submission metadata, sürüm bilgileri ve final dokümanlarının senkronize edilmesi.
6. Faz durumlarının gerçek repo kanıtlarıyla hizalanması ve UI / metin netleştirmeleri.
7. Kullanılmayan Claude odaklı hazırlık yapılarının dokümantasyonda netleştirilmesi.
8. Demo kanıtları, veri yolu anlatımı ve final repo görünümünün temizlenmesi.
