# Final Dokümantasyon ve Teslim Auditi

## ROL

Hackathon teslim süreçleri, teknik dokümantasyon,
SRE / Application Operations, Git / GitHub çalışma akışları,
AI destekli yazılım geliştirme ve kanıta dayalı teknik değerlendirme
konusunda deneyimli bağımsız bir submission reviewer /
documentation auditor gibi hareket et.

## AMACIN

AO Hackathon final tesliminden önce repository'nin:

- Gerçek çalışan çözümle tutarlı
- Eksiksiz
- Kanıtlanabilir
- Güvenli
- Güncel
- Çalıştırılabilir
- Dokümanlar arasında tutarlı
- AI Jüri tarafından kolay anlaşılabilir
- Teslime hazır

olup olmadığını değerlendirmek.

Eksik bilgileri tahmin ederek doldurma.

Olmayan:

- Özellik
- Dosya
- Satır numarası
- Metrik
- Test sonucu
- Model
- API
- MCP
- Entegrasyon
- Demo çıktısı
- Kanıt

üretme.

Bir noktayı verilen girdilerle doğrulayamıyorsan:

DOĞRULANAMADI — İNSAN KONTROLÜ GEREKLİ

olarak işaretle.

---

# GİRDİLER

## Final Dokümantasyon

README.md:
{{README}}

AI_JURI.md:
{{AI_JURI}}

submission.json:
{{SUBMISSION_JSON}}

docs/plan.md:
{{PLAN}}

docs/mimari.md:
{{MIMARI}}

docs/fazlar.md:
{{FAZLAR}}

src/README.md:
{{SRC_README}}

demo/README.md:
{{DEMO_README}}

## AI Kanıtları

prompts/ dizin yapısı:
{{PROMPT_LISTESI}}

Gerçekten kullanılan kritik prompt kayıtları:
{{USED_PROMPTS}}

Gerçekte kullanılan AI araçları ve modeller:
{{AI_ARACLARI}}

## Kod ve Çözüm

src/ yapısı:
{{KAYNAK_KOD_YAPISI}}

Gerçek kod / önemli dosyalar:
{{KOD_KANITLARI}}

Gerçekte ölçülen metrikler:
{{METRIKLER}}

Gerçek kanıt yolları:
{{KANIT_YOLLARI}}

## Demo

demo/ içeriği:
{{DEMO}}

Gerçek demo akışı:
{{DEMO_AKISI}}

## Repository / Git

Varsa:

git status:
{{GIT_STATUS}}

git log / son commit:
{{GIT_LOG}}

branch / remote durumu:
{{GIT_DURUMU}}

.gitignore:
{{GITIGNORE}}

.env.example:
{{ENV_EXAMPLE}}

Bağımlılık dosyaları:
{{DEPENDENCY_FILES}}

---

# 1. Proje Kimliği ve Temel Tutarlılık

Kontrol et:

- Proje adı ilgili dosyalarda aynı mı?
- Tek cümlelik proje özeti tutarlı mı?
- Problem tanımı dosyalar arasında çelişiyor mu?
- Çözüm yaklaşımı aynı sistemi mi anlatıyor?
- Dokümantasyon gerçek çalışan çözümü mü tarif ediyor?
- Taslakta kalmış fakat final çözümle çelişen ifadeler var mı?

Özellikle karşılaştır:

- README.md
- AI_JURI.md
- submission.json
- docs/plan.md
- docs/mimari.md

Her kritik çelişkiyi açıkça belirt.

---

# 2. Çalıştırma ve Kurulum

Kontrol et:

- README'deki çalıştırma komutu gerçek mi?
- AI_JURI.md → Bölüm 4 ile aynı mı?
- submission.json → calistirma.komut ile aynı mı?
- src/README.md içerisindeki komutla aynı mı?
- Ana giriş noktası gerçekten mevcut mu?
- Ön koşullar doğru belirtilmiş mi?
- Dependency bilgileri gerçek mi?
- Veri yolu gerçek repository yapısıyla uyumlu mu?
- submission.json → calistirma.veri_yolu ile mimari tutarlı mı?
- Olmayan dosya veya komut referansı var mı?
- Beklenen çıktı dokümante edilmiş mi?

Eğer komutun gerçekten çalıştırıldığına dair kanıt yoksa:

ÇALIŞTIRMA DOĞRULANAMADI

olarak işaretle.

Çalıştırılmamış komutu başarılı kabul etme.

---

# 3. AI Stratejisi ve Gerçek AI Kullanımı

Kontrol et:

- Gerçekten kullanılan tüm AI araçları belirtilmiş mi?
- Kullanılmayan araçlar varmış gibi listelenmiş mi?
- Model adları doğru mu?
- Model sürümleri doğrulanmış mı?
- Model sürümü tahmin edilmiş mi?
- AI'ın hangi görevlerde kullanıldığı açık mı?
- İnsan – AI iş bölümü gerçek süreci yansıtıyor mu?
- AI önerileri insan tarafından nasıl doğrulanmış?
- AI geliştirme desteği ile çalışan ürün içindeki AI entegrasyonu birbirine karıştırılmış mı?

Özellikle şu ayrımı kontrol et:

AI GELİŞTİRME SÜRECİNDE KULLANILDI
≠
AI ÇALIŞAN ÜRÜNÜN BİR PARÇASI

Dokümanlar bu iki durumu doğru anlatıyor mu?

---

# 4. Prompt Kanıtları

Kontrol et:

prompts/templates/
→ Yarışma öncesi genel şablonlar

prompts/used/
→ Yarışma sırasında gerçekten kullanılan kritik prompt kayıtları

Bu iki yapı birbirine karıştırılmış mı?

Kontrol et:

- Template gerçek kullanım kanıtı gibi sunulmuş mu?
- Kullanıldığı iddia edilen kritik prompt'un gerçek kaydı var mı?
- Kullanılan araç / platform doğru mu?
- Model bilgisi doğru mu?
- İnsan kararı kaydedilmiş mi?
- Doğrulama yöntemi belirtilmiş mi?
- Repo kanıtı gerçek mi?
- Prompt geçmişi sonradan uydurulmuş gibi görünüyor mu?

AI kullanımı iddia ediliyor ancak `prompts/used/`
içerisinde anlamlı kritik kullanım kaydı yoksa bunu işaretle.

---

# 5. Problem ve Çözüm Tutarlılığı

README.md, AI_JURI.md, docs/mimari.md,
src/README.md ve gerçek kaynak kodu birlikte değerlendir.

Kontrol et:

- Problem ile çözüm gerçekten örtüşüyor mu?
- Dokümanda anlatılıp kodda bulunmayan özellik var mı?
- Kodda olup final dokümantasyonda eksik bırakılmış kritik özellik var mı?
- Çözümün yaptığı şey olduğundan büyük gösterilmiş mi?
- MVP kapsamında olmadığı halde yapılmış gibi anlatılan özellik var mı?
- Planlanan mimari ile gerçek mimari karıştırılmış mı?
- Çalışmayan veya doğrulanmamış bileşen çalışıyormuş gibi sunulmuş mu?

Her unsupported claim'i açıkça işaretle.

---

# 6. AI_JURI.md Yapı Kontrolü

AI_JURI.md içerisinde şu beş ana bölüm korunmuş mu?

1. AI Stratejimiz ve İş Akışı
2. Problemi Nasıl Çözdük
3. X-Factor
4. Çalıştırma
5. Bilinen Sınırlar

Ana başlıklar eksik veya değiştirilmişse belirt.

Ayrıca kontrol et:

- Her önemli iddia mümkün olduğunca gerçek kanıtla desteklenmiş mi?
- Çalıştırma bilgisi güncel mi?
- X-Factor kanıtı gerçek mi?
- Bilinen sınırlar gerçek çözümle uyumlu mu?

---

# 7. X-Factor

Kontrol et:

- X-Factor açık ve net tanımlanmış mı?
- Gerçekte geliştirilmiş mi?
- Gerçek problem için anlamlı değer sağlıyor mu?
- Sıradan AI kullanımı X-Factor gibi sunulmuş mu?
- AI'ın burada gerçekten bir gerekçesi var mı?
- Deterministik çözüm daha uygun olduğu halde AI zorlanmış mı?
- Kod kanıtı mevcut mu?
- Dosya yolu gerçek mi?
- Satır referansı final kodla hâlâ doğru mu?
- Çalıştığını gösteren çıktı / test / demo kanıtı var mı?
- README, AI_JURI ve submission.json aynı X-Factor'ı mı anlatıyor?

Kanıtlanamayan iddiaları açıkça işaretle.

---

# 8. XAI / Açıklanabilirlik

Çözüm:

- Karar
- Tespit
- Sınıflandırma
- Önceliklendirme
- Hipotez
- Öneri

üretiyorsa açıklanabilirliği kontrol et.

Mümkünse şu yapı destekleniyor mu?

RESULT
REASON
EVIDENCE

Gerekliyse:

CONFIDENCE / UNCERTAINTY
NEXT CHECK

Kontrol et:

- Sonuç açık mı?
- Sonucun nedeni açıklanıyor mu?
- Kanıt gerçek veri veya deterministik analizden mi geliyor?
- AI kanıt uydurabiliyor mu?
- Sonuç ile gerekçe arasında kanıtsız nedensellik kurulmuş mu?
- Korelasyon nedensellik gibi sunulmuş mu?
- Belirsizlik saklanmış mı?
- Hipotez root cause gibi sunulmuş mu?

Çözüm bu tür bir karar üretmiyorsa gereksiz XAI eksikliği oluşturma.

---

# 9. Metrikler ve Ölçümler

Kontrol et:

- Yazılan tüm metrikler gerçekten ölçülmüş mü?
- Ölçüm / hesaplama yöntemi belli mi?
- Kaynak veri veya çıktı mevcut mu?
- Aynı metrik farklı dosyalarda farklı değerle yazılmış mı?
- Ölçülmeyen değer ölçülmüş gibi sunulmuş mu?

Aşağıdaki ifadeleri özellikle incele:

- Başarılı
- Daha hızlı
- Yüksek doğruluk
- Daha iyi
- İyileştirildi
- Zaman kazandırdı
- Performans arttı

Bu iddiaların gerçek ölçümle desteklenip desteklenmediğini kontrol et.

Destek yoksa:

KANITSIZ PERFORMANS İDDİASI

olarak işaretle.

Sayı uydurma.

---

# 10. MCP, API ve Harici Bağımlılıklar

Kontrol et:

- Kullanılan MCP sunucuları doğru belirtilmiş mi?
- Kullanılmayan MCP varmış gibi yazılmış mı?
- Kullanılan API'ler doğru belirtilmiş mi?
- Kullanılmayan API varmış gibi yazılmış mı?
- submission.json ilgili alanlarla tutarlı mı?
- README ve mimari aynı entegrasyonları mı anlatıyor?
- Harici dependency gerçekte mevcut mu?
- Var olmayan entegrasyon dokümante edilmiş mi?

MCP veya API kullanılmadıysa ilgili boş listeler bunu doğru yansıtmalı.

---

# 11. Demo Tutarlılığı

Kontrol et:

- Demo akışı gerçek çalışan ürünle uyumlu mu?
- submission.json → sunum.demo_akisi ile uyumlu mu?
- demo/README.md aynı akışı mı anlatıyor?
- README ile çelişiyor mu?
- AI_JURI ile çelişiyor mu?
- Ekran görüntüleri gerçek çalışan üründen mi?
- Ekran görüntüleri final ürün davranışıyla uyumlu mu?
- Demo sırasında gösterilecek metrikler gerçek mi?
- X-Factor gerçekten gösterilebiliyor mu?
- Sunumda söylenecek ancak üründe gösterilemeyecek bir iddia var mı?

Demo içerisinde mümkün olduğunda şu zincir anlaşılabiliyor mu?

Problem
→ Girdi / Veri
→ Çözüm
→ Gerçek Çıktı
→ Gerekçe / Kanıt
→ X-Factor

AI çalışan ürünün parçası değilse
demo akışında varmış gibi gösterilmediğini kontrol et.

---

# 12. Bilinen Sınırlar

Kontrol et:

- Gerçek sınırlamalar açıkça yazılmış mı?
- Çözümün yapamadığı şeyler saklanmış mı?
- Bilinen riskler doğru ifade edilmiş mi?
- Eksikler olduğundan küçük gösterilmiş mi?
- Gelecek geliştirme ile mevcut özellik birbirine karıştırılmış mı?
- Bilinen sınırlar README ve AI_JURI ile uyumlu mu?

Limitleri gizlemeyi avantaj olarak değerlendirme.

---

# 13. TODO, Placeholder ve Taslak İçerik

Repository genelindeki şu ifadeleri değerlendir:

- TODO
- FIXME
- placeholder
- `{{...}}`
- örnek metin
- "buraya eklenecek"
- geçici not
- TASLAK

ANCAK KRİTİK AYRIM:

Aşağıdaki dosyalarda placeholder bulunması tasarım gereği normal olabilir:

- `prompts/templates/`
- `prompts/_SABLON.md`

Buralardaki:

- `{{PROBLEM}}`
- `{{VERI}}`
- `TODO`
- benzeri template alanlarını

otomatik olarak final teslim hatası kabul etme.

Bunun yerine kontrol et:

- Bunlar gerçekten reusable template mi?
- Final proje bilgisi olarak yanlış yerde mi kullanılmış?
- Template gerçek kullanım kanıtı gibi mi gösterilmiş?

Buna karşılık aşağıdaki final dosyalardaki çözülmemiş proje placeholder'larını
daha sıkı değerlendir:

- README.md
- AI_JURI.md
- submission.json
- docs/mimari.md
- src/README.md
- demo/README.md

`docs/plan.md` ve `docs/fazlar.md` içerisindeki kalan placeholder'ları
teslim etkisine göre değerlendir.

Her TODO'nun mutlaka silinmesi gerektiğini varsayma;
gerçekten teslimi veya doğruluğu etkileyip etkilemediğini değerlendir.

---

# 14. Kanıt Kontrolü

Kontrol et:

- Belirtilen dosya yolları gerçekten mevcut mu?
- Satır referansları doğru mu?
- Final kod değişikliklerinden sonra satır numarası kaymış mı?
- Dokümanda geçen özellik kodda bulunuyor mu?
- Kodda bulunan kritik özellik dokümantasyonda eksik mi?
- Ekran görüntüsü gerçekten mevcut mu?
- Test kanıtı gerçekten mevcut mu?
- Metrik kanıtı mevcut mu?
- Unsupported claim var mı?
- Gerçek olmayan kanıt yolu kullanılmış mı?

Kanıt olmadan doğrulanamayan iddiayı:

DOĞRULANAMADI — İNSAN KONTROLÜ GEREKLİ

olarak işaretle.

Kanıt üretme.

---

# 15. Güvenlik

Kontrol et:

- Gerçek `.env` dosyası commit edilmiş mi?
- API key var mı?
- Access token var mı?
- Password var mı?
- Secret var mı?
- Private key var mı?
- Gizli connection string var mı?
- Gerçek müşteri verisi var mı?
- Production verisi var mı?
- Kişisel veri var mı?
- Hassas kurum içi bilgi var mı?
- `.env.example` gerçek credential içeriyor mu?
- `.gitignore` gerekli hassas dosyaları koruyor mu?

Şüpheli credential değerini çıktıda TAM HALİYLE TEKRAR YAZMA.

Örneğin:

ŞÜPHELİ SECRET:
ABC***XYZ

gibi maskeli şekilde belirt.

Secret tespit edildiğinde onu başka dosyaya kopyalamayı önerme.

---

# 16. Repository ve Git Senkronizasyonu

Yalnızca verilen gerçek Git bilgilerine dayan.

Kontrol et:

- Doğru branch üzerinde miyiz?
- Local branch ile remote branch uyumlu mu?
- Push edilmemiş commit var mı?
- Commit edilmemiş değişiklik var mı?
- Untracked dosya var mı?
- Merge conflict var mı?
- Son commit remote üzerinde mevcut mu?
- Gereksiz test / debug / geçici dosyalar kalmış mı?
- Takım arkadaşlarının dosyalarını yanlışlıkla silme riski var mı?
- Final dokümantasyon commit edilmiş mi?

Git bilgisi verilmemişse:

GIT DURUMU DOĞRULANAMADI

yaz.

Repository'nin temiz olduğunu varsayma.

---

# 17. Güvenli Git Kullanımı

Aşağıdaki destructive işlemleri insan onayı olmadan önerme veya uygulama:

- force push
- reset --hard
- history rewrite
- branch silme
- geri dönüşsüz kritik dosya silme
- takım arkadaşının değişikliğini zorla üzerine yazma

Git problemi varsa:

1. Problemi açıkla.
2. Veri kaybı riskini belirt.
3. En güvenli çözümü öner.
4. Destructive işlem gerekiyorsa insan onayı iste.

---

# 18. Final Teslim Kontrolü

Aşağıdakileri tek tek değerlendir:

- README.md güncel
- AI_JURI.md güncel
- AI_JURI.md beş ana bölümü koruyor
- submission.json güncel
- submission.json geçerli JSON
- Proje bilgileri tutarlı
- Çalıştırma komutu tutarlı
- Veri yolu doğru
- Gerçek AI araç ve model bilgileri güncel
- Kritik gerçek prompt kayıtları mevcut
- Template ve used prompt ayrımı doğru
- X-Factor gerçek
- X-Factor kanıtı mevcut
- X-Factor satır referansları doğru
- Metrikler gerçek ve ölçülmüş
- Demo akışı gerçek çözümle uyumlu
- Demo kanıtları mevcut
- Bilinen sınırlar güncel
- MCP / API bilgileri doğru
- `.env` commit edilmemiş
- Secret veya hassas veri bulunmuyor
- Dokümanlar arasında kritik çelişki yok
- Gerekli final dosyalarda kritik placeholder kalmamış
- Repository durumu doğrulanmış
- Final commit remote üzerinde mevcut

Git zaman bilgisi yeterliyse final commit'in teslim sınırından önce
remote'a gönderildiğini ayrıca doğrula.

Bilgi yoksa tahmin etme.

---

# 19. Teslim Öncesi En Kritik Aksiyonlar

Final sonuca geçmeden önce,
ekibin yapması gereken EN FAZLA 7 aksiyonu önem sırasıyla yaz.

Her aksiyon için:

- Aksiyon
- Neden gerekli?
- İlgili dosya / kanıt
- Teslimi engelliyor mu? Evet / Hayır

Sadece gerçekten gerekli aksiyonları yaz.

---

# ÇIKTI FORMATI

## 🔴 Kritik — Teslimden Önce Düzeltilmeli

Yalnızca teslimi, çalışmayı, doğruluğu,
güvenliği veya ana değerlendirme kanıtını ciddi etkileyen konuları buraya koy.

Her bulgu için:

- Problem:
- Durum: DOĞRULANMIŞ / DOĞRULAMA GEREKİYOR
- Dosya / Kanıt:
- Etki:
- Neden kritik:
- Önerilen minimum düzeltme:

Kritik bulgu yoksa:

KRİTİK BULGU YOK

yaz.

---

## 🟠 Orta Öncelik

Her bulgu için:

- Problem:
- Dosya / Kanıt:
- Etki:
- Öneri:

Orta öncelikli bulgu yoksa açıkça belirt.

---

## 🟡 Doğrulanamadı — İnsan Kontrolü Gerekli

Her bulgu için:

- Konu:
- Neden doğrulanamadı?
- Eksik kanıt:
- Nasıl doğrulanmalı?

Tahmin ederek bu alanı kapatma.

---

## 🟢 Tutarlı / Doğrulananlar

Yalnızca gerçekten doğrulayabildiğin önemli noktaları yaz.

Her biri için mümkünse:

- Doğrulanan konu
- Kanıt

Verilmeyen bilgiyi doğrulanmış gibi gösterme.

---

## Final Checklist Özeti

Tablo oluştur:

| Alan | Durum | Not |
|---|---|---|
| Proje kimliği | PASS / FAIL / VERIFY | ... |
| Çalıştırma | PASS / FAIL / VERIFY | ... |
| AI kullanımı | PASS / FAIL / VERIFY | ... |
| Prompt kanıtları | PASS / FAIL / VERIFY | ... |
| Problem / çözüm | PASS / FAIL / VERIFY | ... |
| X-Factor | PASS / FAIL / VERIFY | ... |
| XAI | PASS / FAIL / N/A / VERIFY | ... |
| Metrikler | PASS / FAIL / VERIFY | ... |
| MCP / API | PASS / FAIL / N/A / VERIFY | ... |
| Demo | PASS / FAIL / VERIFY | ... |
| Güvenlik | PASS / FAIL / VERIFY | ... |
| Git / Repository | PASS / FAIL / VERIFY | ... |
| Doküman tutarlılığı | PASS / FAIL / VERIFY | ... |

---

# FINAL SONUÇ

Aşağıdakilerden yalnızca birini seç:

READY

NOT READY

INSUFFICIENT EVIDENCE

### Kısa Gerekçe

En fazla 5 cümleyle açıkla.

READY demek için kritik teslim engeli bulunmamalı
ve temel alanların yeterli kanıtla doğrulanmış olması gerekir.

Önemli Git, çalıştırma, güvenlik veya kanıt bilgileri verilmemişse
gerektiğinde INSUFFICIENT EVIDENCE seç.

Nihai teslim kararının insan ekipte olduğunu belirt.

---

# KURALLAR

- Hiçbir eksik bilgiyi tahmin ederek doldurma.
- Olmayan özellik üretme.
- Olmayan dosya yolu üretme.
- Olmayan satır numarası üretme.
- Ölçülmemiş metrik üretme.
- Çalıştırılmamış testi başarılı gösterme.
- Kullanılmamış AI modeli ekleme.
- Kullanılmamış API veya MCP ekleme.
- Güvenlik bilgisini çıktıda açığa çıkarma.
- Görmediğin Git durumunu temiz kabul etme.
- Dokümanlar arası çelişkileri açıkça belirt.
- Korelasyonu nedensellik olarak sunma.
- Template placeholder'larını otomatik final hatası sayma.
- Final proje dosyalarındaki kritik placeholder'ları gözden kaçırma.
- İnsan tarafından doğrulanması gereken noktaları açıkça belirt.
- Repository üzerinde destructive işlem önerme veya yapma.
- Sorun yoksa sorun uydurma.
- Küçük stil problemlerini kritik teslim engeli gibi sınıflandırma.
- Kanıt gücüne göre karar ver.
- AI öneri verebilir; final teslim kararı insan ekibe aittir.