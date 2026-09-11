# Fazlar

> **Durum: TASLAK**
>
> Bu dosya hackathon öncesi hazırlıkları ve hackathon sırasında çözümün hangi aşamada olduğunu takip etmek için kullanılacaktır.
>
> Senaryo henüz açıklanmadığı için çözüme özel adımlar genel tutulmuştur.
> Senaryo ve veri paketi paylaşıldıktan sonra faz içerikleri gerçek çalışma adımlarına göre güncellenecektir.

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

**Durum:** beklemede

Senaryo ve veri paketi paylaşıldığında önce problemin doğru anlaşılması ve uygulanabilir bir yaklaşım belirlenmesi hedeflenecektir.

- [ ] Senaryo ekip tarafından birlikte okundu
- [ ] Beklenen görev ve çıktı netleştirildi
- [ ] Problem kısa ve somut şekilde tanımlandı
- [ ] Açık sorular belirlendi
- [ ] Gerekli sorular toplu soru penceresinde soruldu
- [ ] İlk başarı kriterleri belirlendi
- [ ] Veri paketinin formatı ve yapısı incelendi
- [ ] Önemli olabilecek alanlar ve sinyaller belirlendi
- [ ] İlk gözlemler kaydedildi
- [ ] İlk hipotezler oluşturuldu
- [ ] Hipotezlerin doğrulama yöntemleri belirlendi
- [ ] Alternatif çözüm yaklaşımları değerlendirildi
- [ ] MVP kapsamı belirlendi
- [ ] Ana çözüm yaklaşımı seçildi
- [ ] İnsan – AI iş bölümü netleştirildi
- [ ] İlk geliştirme planı oluşturuldu
- [ ] Kullanılan kritik planlama / veri keşfi prompt'ları kaydedildi
- [ ] `docs/plan.md` gerçek bilgilerle güncellendi

> **Not:** İlk aşamada doğrudan kapsamlı kod geliştirmeye geçmek yerine problem, veri ve yaklaşımın netleştirilmesine öncelik verilmelidir.
>
> Hipotezler kanıtlanmış sonuç değildir; veri ile desteklenmeli, zayıflatılmalı veya elenmelidir.

---

## Faz 2 — Geliştirme, Analiz ve Doğrulama

**Durum:** beklemede

Seçilen yaklaşım mümkün olduğunca küçük, test edilebilir ve doğrulanabilir parçalar halinde geliştirilecektir.

### Temel Geliştirme

- [ ] Veri girdisi / okuma mekanizması oluşturuldu
- [ ] Gerekli veri hazırlama adımları tamamlandı
- [ ] Senaryonun beklediği temel çözüm mantığı geliştirildi
- [ ] Çekirdek modüller ayrı ayrı çalıştırıldı
- [ ] İlk uçtan uca çalışan akış oluşturuldu

### Analiz ve Doğrulama

- [ ] İlk hipotezler gerçek verilerle karşılaştırıldı
- [ ] Kritik sonuçlar veri veya test çıktılarıyla doğrulandı
- [ ] Kanıtlanmayan nedensellik iddiaları kontrol edildi
- [ ] Hatalar ve önemli edge case'ler incelendi
- [ ] Çözüm uçtan uca yeniden çalıştırıldı

### AI Kullanımı

- [ ] AI'ın gerçekten ihtiyaç duyulduğu noktalar belirlendi
- [ ] Gerekli AI entegrasyonları çalışır hale getirildi
- [ ] AI çıktıları insan tarafından doğrulandı
- [ ] Kullanılan AI araçları ve gerçek model sürümleri kaydedildi
- [ ] Kritik kullanılan prompt'lar kaydedildi
- [ ] Gerekiyorsa model karşılaştırması gerçekleştirildi

### Açıklanabilirlik ve X-Factor

- [ ] Çözüm karar / tespit / öneri üretiyorsa açıklanabilirlik yaklaşımı oluşturuldu
- [ ] Sonuçların gerekçe ve kanıtları gösterilebilir hale getirildi
- [ ] Çözüm için anlamlı X-Factor netleştirildi
- [ ] X-Factor gerçek üründe çalışır hale getirildi
- [ ] X-Factor'ın kod ve/veya çıktı kanıtı oluşturuldu

### Ölçüm ve Teknik Kanıt

- [ ] Senaryoya uygun gerçek metrikler ölçüldü
- [ ] Metriklerin hesaplama yöntemi kaydedildi
- [ ] `docs/mimari.md` gerçek çözümle güncellendi
- [ ] Anlamlı ara commit'ler oluşturuldu

> **Not:** Büyük ve doğrulanmamış tek bir kod üretimi yerine modül bazlı geliştirme, çalıştırma ve doğrulama tercih edilmelidir.
>
> Final durumda yalnızca gerçekten gerçekleştirilen maddeler tamamlandı olarak işaretlenmelidir.

---

## Faz 3 — Dokümantasyon ve Jüri Hazırlığı

**Durum:** beklemede

Final dokümantasyon gerçek çalışan çözüm ve gerçek kanıtlarla güncellenecektir.

### README

- [ ] `README.md` gerçek proje bilgileriyle güncellendi
- [ ] Proje adı ve tek cümlelik özet netleştirildi
- [ ] Çözülen problem açık şekilde anlatıldı
- [ ] Çözümün uçtan uca nasıl çalıştığı açıklandı
- [ ] Kurulum adımları güncellendi
- [ ] Çalıştırma komutu doğrulandı
- [ ] Beklenen çıktı açıklandı
- [ ] Kullanılan tüm AI araçları ve gerçek model sürümleri yazıldı
- [ ] İnsan – AI iş bölümü gerçek süreçle güncellendi
- [ ] XAI / açıklanabilirlik yaklaşımı gerekiyorsa açıklandı
- [ ] X-Factor açıklandı ve kanıtlandı
- [ ] Gerçek ölçümler eklendi
- [ ] Bilinen sınırlar açıklandı

### MCP ve API

- [ ] Kullanılan MCP sunucuları belirtildi
- [ ] MCP kullanılmadıysa açıkça belirtilmesi kontrol edildi
- [ ] Kullanılan API'ler belirtildi
- [ ] Harici API kullanılmadıysa açıkça belirtilmesi kontrol edildi
- [ ] Gizli erişim bilgisi dokümantasyona eklenmedi

### AI Jüri ve Submission

- [ ] `AI_JURI.md` beş ana bölüm altında gerçek bilgilerle tamamlandı
- [ ] Önemli iddialar gerçek kanıt yollarıyla desteklendi
- [ ] X-Factor için gerçek dosya / satır aralığı doğrulandı
- [ ] `submission.json` gerçek bilgilerle tamamlandı
- [ ] `submission.json` geçerli JSON olarak doğrulandı
- [ ] README / AI_JURI / submission ortak alanları karşılaştırıldı
- [ ] Çalıştırma komutu üç dosyada da tutarlı
- [ ] Model adları ve sürümleri ilgili dokümanlarda tutarlı
- [ ] Ölçülen metrikler ilgili dokümanlarda tutarlı
- [ ] Bilinen sınırlar final çözümle uyumlu

### Prompt Kanıtları

- [ ] Yarışma sırasında gerçekten kullanılan kritik prompt'lar `prompts/used/` altında kaydedildi
- [ ] Prompt kayıtlarında kullanılan araç / model bilgileri belirtildi
- [ ] İnsan kararı ve doğrulama adımları kaydedildi
- [ ] Var olmayan kanıt yolu veya sonuç yazılmadı

---

## Faz 4 — Demo ve Final Teslim

**Durum:** beklemede

### Çalıştırma ve Demo

- [ ] Uygulama baştan sona yeniden çalıştırıldı
- [ ] Kurulum adımları yeniden kontrol edildi
- [ ] Final çalıştırma komutu test edildi
- [ ] Beklenen çıktı doğrulandı
- [ ] Demo akışı hazırlandı
- [ ] Demo akışı gerçek ürünle uçtan uca test edildi
- [ ] Gerekli ekran görüntüleri `demo/` altına eklendi
- [ ] Varsa demo video bağlantısı dokümante edildi
- [ ] Sunum akışı hazırlandı
- [ ] Demo sırasında gösterilecek X-Factor kanıtı hazır
- [ ] Demo sırasında gösterilecek metrikler doğrulandı

### Güvenlik Kontrolü

- [ ] Gerçek `.env` dosyasının commit edilmediği doğrulandı
- [ ] `.env.example` güncel ve gizli bilgi içermiyor
- [ ] API key, token, parola veya secret bulunmadığı kontrol edildi
- [ ] Gerçek müşteri / production verisi bulunmadığı kontrol edildi
- [ ] Hassas veya kişisel veri bulunmadığı kontrol edildi

### Repository Kontrolü

- [ ] Repo public durumda
- [ ] Gereksiz test / debug / geçici dosyalar kontrol edildi
- [ ] `TODO`, `FIXME` ve placeholder alanları kontrol edildi
- [ ] `AI_JURI.md` güncel
- [ ] `submission.json` güncel
- [ ] README güncel
- [ ] X-Factor dosya ve satır referansları final kodla yeniden doğrulandı
- [ ] `git status` kontrol edildi
- [ ] Commit edilmemiş kritik değişiklik kalmadı
- [ ] Merge conflict bulunmuyor
- [ ] Local / remote durumu kontrol edildi

### Final Teslim

- [ ] Final commit oluşturuldu
- [ ] Final push tamamlandı
- [ ] GitHub üzerindeki final commit doğrulandı
- [ ] Repo final push sonrasında tekrar kontrol edildi
- [ ] Teslim saatinden önce gönderimin tamamlandığı doğrulandı

> **KRİTİK:** Değerlendirme 17:30'daki son commit üzerinden yapılacaktır.
> Final push son dakikaya bırakılmamalıdır.