# Fazlar

Bu dosya hackathon hazırlıklarını ve S-A1 Alarm Fırtınası çözümü için gerçekleştirilen çalışmaları takip eder.

**Durum değerleri:**

- `beklemede`
- `devam ediyor`
- `tamamlandı`
- `iptal`

---

## Faz 0 — Hazırlık ve Kurulum

**Durum:** devam ediyor

Hackathon başlamadan önce tamamlanması gereken hazırlıklar:

- [x] GitHub repo oluşturuldu
- [x] Repo public olarak ayarlandı
- [x] Zorunlu dosya ve klasör iskeleti oluşturuldu
- [x] SAKA erişimi kontrol edildi
- [x] Git kurulumu doğrulandı
- [x] Python / Node geliştirme ortamı kontrol edildi
- [x] Repo lokal ortama clone edildi
- [x] `git pull` bağlantısı test edildi
- [ ] Tüm ekip üyelerinin GitHub erişimi doğrulandı
- [ ] Deneme commit / push işlemi tüm ekip üyeleri için doğrulandı
- [ ] Ekip üyelerinin temel görev ve sorumlulukları netleştirildi
- [ ] Başlangıç teknoloji tercihleri netleştirildi
- [ ] `.gitignore` içerisinde `.env` koruması doğrulandı
- [ ] SAKA üzerinden gerçek bir test model çağrısı gerçekleştirildi
- [ ] Gerekli geliştirme araçlarının yarışma günü kullanılabilir olduğu doğrulandı

> **Not:** Hackathon günü kurulum ve erişim problemleriyle zaman kaybetmemek için bu faz etkinlikten önce mümkün olduğunca tamamlanmalıdır.

---

## Faz 1 — Senaryo Analizi ve Planlama

**Durum:** tamamlandı

Senaryo ve veri paketi paylaşıldığında önce problemin doğru anlaşılması ve uygulanabilir bir yaklaşım belirlenmesi hedeflenecektir.

- [x] Senaryo ekip tarafından birlikte okundu
- [x] Beklenen görev ve çıktı netleştirildi
- [x] Problem kısa ve somut şekilde tanımlandı
- [x] Açık sorular belirlendi
- [ ] Gerekli sorular toplu soru penceresinde soruldu
- [x] İlk başarı kriterleri belirlendi
- [x] Veri paketinin formatı ve yapısı incelendi
- [x] Önemli olabilecek alanlar ve sinyaller belirlendi
- [x] İlk gözlemler kaydedildi
- [x] İlk hipotezler oluşturuldu
- [x] Hipotezlerin doğrulama yöntemleri belirlendi
- [x] Alternatif çözüm yaklaşımları değerlendirildi
- [x] MVP kapsamı belirlendi
- [x] Ana çözüm yaklaşımı seçildi
- [x] İnsan – AI iş bölümü netleştirildi
- [x] İlk geliştirme planı oluşturuldu
- [x] Kullanılan kritik planlama / veri keşfi prompt'ları kaydedildi
- [x] `docs/plan.md` gerçek bilgilerle güncellendi

> **Not:** İlk aşamada doğrudan kapsamlı kod geliştirmeye geçmek yerine problem, veri ve yaklaşımın netleştirilmesine öncelik verilmelidir.
>
> Hipotezler kanıtlanmış sonuç değildir; veri ile desteklenmeli, zayıflatılmalı veya elenmelidir.

---

## Faz 2 — Geliştirme, Analiz ve Doğrulama

**Durum:** tamamlandı

Seçilen yaklaşım mümkün olduğunca küçük, test edilebilir ve doğrulanabilir parçalar halinde geliştirilecektir.

### Temel Geliştirme

- [x] Veri girdisi / okuma mekanizması oluşturuldu
- [x] Gerekli veri hazırlama adımları tamamlandı
- [x] Senaryonun beklediği temel çözüm mantığı geliştirildi
- [x] Çekirdek modüller ayrı ayrı çalıştırıldı
- [x] İlk uçtan uca çalışan akış oluşturuldu

### Analiz ve Doğrulama

- [x] İlk hipotezler gerçek verilerle karşılaştırıldı
- [x] Kritik sonuçlar veri veya test çıktılarıyla doğrulandı
- [x] Kanıtlanmayan nedensellik iddiaları kontrol edildi
- [x] Hatalar ve önemli edge case'ler incelendi
- [x] Çözüm uçtan uca yeniden çalıştırıldı

### AI Kullanımı

- [x] AI'ın gerçekten ihtiyaç duyulduğu noktalar belirlendi
- [x] Çalışan ürün içinde canlı AI entegrasyonu kullanılmamasına karar verildi
- [x] AI çıktıları insan tarafından doğrulandı
- [x] Kullanılan AI araçları kaydedildi; model sürümü final öncesi doğrulanacak
- [x] Kritik kullanılan prompt'lar kaydedildi
- [ ] Gerekiyorsa model karşılaştırması gerçekleştirildi

### Açıklanabilirlik ve X-Factor

- [x] Çözüm karar / tespit / öneri üretiyorsa açıklanabilirlik yaklaşımı oluşturuldu
- [x] Sonuçların gerekçe ve kanıtları gösterilebilir hale getirildi
- [x] Çözüm için anlamlı X-Factor netleştirildi
- [x] X-Factor gerçek üründe çalışır hale getirildi
- [x] X-Factor'ın kod ve/veya çıktı kanıtı oluşturuldu

### Ölçüm ve Teknik Kanıt

- [x] Senaryoya uygun gerçek metrikler ölçüldü
- [x] Metriklerin hesaplama yöntemi kaydedildi
- [x] `docs/mimari.md` gerçek çözümle güncellendi
- [ ] Anlamlı ara commit'ler oluşturuldu

> **Not:** Büyük ve doğrulanmamış tek bir kod üretimi yerine modül bazlı geliştirme, çalıştırma ve doğrulama tercih edilmelidir.
>
> Final durumda yalnızca gerçekten gerçekleştirilen maddeler tamamlandı olarak işaretlenmelidir.

---

## Faz 3 — Dokümantasyon ve Jüri Hazırlığı

**Durum:** devam ediyor

Final dokümantasyon gerçek çalışan çözüm ve gerçek kanıtlarla güncellenecektir.

### README

- [x] `README.md` gerçek proje bilgileriyle güncellendi
- [x] Proje adı ve tek cümlelik özet netleştirildi
- [x] Çözülen problem açık şekilde anlatıldı
- [x] Çözümün uçtan uca nasıl çalıştığı açıklandı
- [x] Kurulum adımları güncellendi
- [x] Çalıştırma komutu doğrulandı
- [x] Beklenen çıktı açıklandı
- [x] Kullanılan tüm AI araçları ve gerçek model sürümleri yazıldı
- [x] İnsan – AI iş bölümü gerçek süreçle güncellendi
- [x] XAI / açıklanabilirlik yaklaşımı gerekiyorsa açıklandı
- [x] X-Factor açıklandı ve kanıtlandı
- [x] Gerçek ölçümler eklendi
- [x] Bilinen sınırlar açıklandı

### MCP ve API

- [ ] Kullanılan MCP sunucuları belirtildi
- [x] MCP kullanılmadıysa açıkça belirtilmesi kontrol edildi
- [ ] Kullanılan API'ler belirtildi
- [x] Harici API kullanılmadıysa açıkça belirtilmesi kontrol edildi
- [ ] Gizli erişim bilgisi dokümantasyona eklenmedi

### AI Jüri ve Submission

- [x] `AI_JURI.md` beş ana bölüm altında gerçek bilgilerle tamamlandı
- [x] Önemli iddialar gerçek kanıt yollarıyla desteklendi
- [ ] X-Factor için gerçek dosya / satır aralığı doğrulandı
- [x] `submission.json` gerçek bilgilerle tamamlandı
- [x] `submission.json` geçerli JSON olarak doğrulandı
- [x] README / AI_JURI / submission ortak alanları karşılaştırıldı
- [x] Çalıştırma komutu üç dosyada da tutarlı
- [x] Model adları ve sürümleri ilgili dokümanlarda tutarlı
- [x] Ölçülen metrikler ilgili dokümanlarda tutarlı
- [x] Bilinen sınırlar final çözümle uyumlu

### Prompt Kanıtları

- [x] Yarışma sırasında gerçekten kullanılan kritik prompt'lar `prompts/used/` altında kaydedildi
- [x] Prompt kayıtlarında kullanılan araç / model bilgileri belirtildi
- [ ] İnsan kararı ve doğrulama adımları kaydedildi
- [ ] Var olmayan kanıt yolu veya sonuç yazılmadı

---

## Faz 4 — Demo ve Final Teslim

**Durum:** devam ediyor

### Çalıştırma ve Demo

- [x] Uygulama baştan sona yeniden çalıştırıldı
- [ ] Kurulum adımları yeniden kontrol edildi
- [x] Final çalıştırma komutu test edildi
- [x] Beklenen çıktı doğrulandı
- [x] Demo akışı hazırlandı
- [ ] Demo akışı gerçek ürünle uçtan uca test edildi
- [x] Gerekli ekran görüntüleri `demo/` altına eklendi
- [ ] Varsa demo video bağlantısı dokümante edildi
- [ ] Sunum akışı hazırlandı
- [ ] Demo sırasında gösterilecek X-Factor kanıtı hazır
- [x] Demo sırasında gösterilecek metrikler doğrulandı

### Güvenlik Kontrolü

- [x] Gerçek `.env` dosyasının commit edilmediği doğrulandı
- [x] `.env.example` güncel ve gizli bilgi içermiyor
- [ ] API key, token, parola veya secret bulunmadığı kontrol edildi
- [ ] Gerçek müşteri / production verisi bulunmadığı kontrol edildi
- [ ] Hassas veya kişisel veri bulunmadığı kontrol edildi

### Repository Kontrolü

- [ ] Repo public durumda
- [ ] Gereksiz test / debug / geçici dosyalar kontrol edildi
- [ ] Yer tutucu ve düzeltme notları kontrol edildi
- [x] `AI_JURI.md` güncel
- [x] `submission.json` güncel
- [x] README güncel
- [ ] X-Factor dosya ve satır referansları final kodla yeniden doğrulandı
- [x] `git status` kontrol edildi
- [ ] Commit edilmemiş kritik değişiklik kalmadı
- [x] Merge conflict bulunmuyor
- [x] Local / remote durumu kontrol edildi

### Final Teslim

- [ ] Final commit oluşturuldu
- [ ] Final push tamamlandı
- [ ] GitHub üzerindeki final commit doğrulandı
- [ ] Repo final push sonrasında tekrar kontrol edildi
- [ ] Teslim saatinden önce gönderimin tamamlandığı doğrulandı

> **KRİTİK:** Değerlendirme 17:30'daki son commit üzerinden yapılacaktır.
> Final push son dakikaya bırakılmamalıdır.