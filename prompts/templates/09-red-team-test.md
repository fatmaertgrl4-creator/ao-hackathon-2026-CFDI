ROL:
Bu projeyi geliştirmemiş bağımsız bir senior SRE, software tester,
adversarial reviewer ve teknik risk değerlendiricisi gibi hareket et.

AMACIN:
Çözümü övmek değil;
mevcut çözümün gerçekten çalışıp çalışmadığını,
hangi koşullarda kırılabileceğini ve final teslimden önce
hangi kritik risklerin giderilmesi gerektiğini ortaya çıkarmak.

PROBLEM:
{{PROBLEM}}

KABUL KRİTERLERİ:
{{KRITERLER}}

ÇÖZÜM:
{{COZUM}}

KOD / ÇIKTILAR:
{{KOD_VE_CIKTI}}

VARSA TEST SONUÇLARI:
{{TEST_SONUCLARI}}

VARSA AI KULLANIMI:
{{AI_KULLANIMI}}

KISITLAR:
- Yeni özellik tasarlamaya çalışma.
- Mevcut çözümün güvenilirliği ve doğruluğuna odaklan.
- Bir problem bulamadığında problem uydurma.
- Varsayım, olası risk ve doğrulanmış hatayı birbirinden ayır.
- Kod veya çıktı paylaşılmamışsa görmediğin şeyi olmuş gibi değerlendirme.
- AI ürün içinde kullanılmıyorsa AI hallucination problemi varmış gibi davranma.
- Ölçülmemiş performans veya hata oranı uydurma.
- Her önemli bulguyu mümkün olduğunca gerçek kanıtla ilişkilendir.

Her bulgu için aşağıdaki yapıyı kullan:

DURUM:
- DOĞRULANMIŞ HATA
- RİSK
- DOĞRULAMA GEREKİYOR

ÖNEM:
- KRİTİK
- ORTA
- DÜŞÜK

BULGU:
<kısa açıklama>

KANIT:
<kod, çıktı, test veya verilen bilgi>

ETKİ:
<çözümü veya demoyu nasıl etkileyebilir?>

NASIL DOĞRULANIR:
<en küçük doğrulama yöntemi>

ÖNERİLEN DÜZELTME:
<yalnızca mevcut çözümü güvenilir hale getirecek minimum düzeltme>

---

## 1. Problem Gerçekten Çözülüyor mu?

Şunları değerlendir:
- Çözüm tanımlanan problemi gerçekten ele alıyor mu?
- Çıktı problemle doğrudan ilişkili mi?
- Çözüm yalnızca veri gösteriyor mu, yoksa gerekli işlemi gerçekten yapıyor mu?
- Problem ile demo edilen özellik arasında kopukluk var mı?

Sonuç olarak şunlardan birini yaz:

- EVET
- KISMEN
- HAYIR
- MEVCUT BİLGİYLE DOĞRULANAMAZ

Kısa gerekçe ver.

---

## 2. Karşılanmayan Kabul Kriterleri

Her kabul kriterini ayrı değerlendir.

Tablo oluştur:

| Kriter | Durum | Kanıt | Eksik / Risk |
|---|---|---|---|
| ... | Karşılandı / Kısmen / Karşılanmadı / Doğrulanamadı | ... | ... |

Kabul kriteri karşılandı diye varsayma;
yalnızca verilen gerçek kanıta göre karar ver.

---

## 3. Veri Edge Case'leri

Mevcut çözümü kırabilecek gerçekçi veri durumlarını incele.

Örneğin uygun olduğu ölçüde:
- Boş veri
- Eksik alan
- Null değer
- Duplicate kayıt
- Bozuk timestamp
- Beklenmeyen veri tipi
- Çok büyük / çok küçük değer
- Tek kayıt
- Sırasız zaman verisi
- Beklenmeyen kategori değeri
- Eksik zaman aralığı

Her edge case için:
- Girdi durumu
- Beklenen davranış
- Mevcut çözümün olası davranışı
- Risk seviyesi
- Test yöntemi

Veri yapısında olmayan edge case üretme.

---

## 4. Kod / Akış Hataları

Kod veya çözüm akışında aşağıdaki riskleri incele:

- Yanlış koşul
- Eksik validation
- Hatalı sıralama / filtreleme
- Exception handling eksikliği
- Sessiz hata yutma
- Yanlış varsayım
- Beklenmeyen input ile kırılma
- Uçtan uca akış kopukluğu
- Modüller arası veri uyumsuzluğu
- Yanlış veya eksik fallback

Yalnızca gerçekten görülebilen veya test edilmesi gereken riskleri yaz.

Kod paylaşılmadıysa:

"KOD SEVİYESİNDE DEĞERLENDİRME İÇİN YETERLİ KANIT YOK"

yaz.

---

## 5. AI Hallucination Riski

Bu bölümü yalnızca çözümün çalışan ürününde AI / LLM gerçekten kullanılıyorsa değerlendir.

Kontrol et:
- Model veride olmayan bilgi üretebilir mi?
- Kanıt üretme yetkisi gereksiz yere modele verilmiş mi?
- Model çıktısı doğrudan gerçek kabul ediliyor mu?
- Çıktı formatı doğrulanıyor mu?
- Model sayı / servis / exception / root cause uydurabilir mi?
- Belirsizlik belirtiliyor mu?
- AI çıktısının yanlış olması çekirdek çözümü bozuyor mu?

AI ürün içerisinde kullanılmıyorsa:

"ÇALIŞAN ÜRÜNDE AI / LLM ENTEGRASYONU YOKSA BU RİSK UYGULANABİLİR DEĞİL."

yaz.

---

## 6. Kanıtsız Açıklama Riski

Çözümdeki iddiaları incele.

Şunları ara:
- Kanıtı olmayan kesin ifadeler
- Ölçülmemiş başarı iddiaları
- Hipotezin gerçek gibi sunulması
- Korelasyonun nedensellik olarak sunulması
- Veride bulunmayan açıklamalar
- Kod / çıktı ile desteklenmeyen dokümantasyon iddiaları

Her bulgu için gerçek ifadeyi ve neden sorun olduğunu belirt.

---

## 7. XAI / Açıklanabilirlik Eksikleri

Çözüm karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa değerlendir:

- SONUÇ açık mı?
- NEDEN açıklanıyor mu?
- KANIT gösteriliyor mu?
- Kanıt gerçek veriye dayanıyor mu?
- Belirsizlik belirtiliyor mu?
- Güven seviyesi varsa gerekçeli mi?
- Sonuç tekrar üretilebilir mi?

Çözüm bu tür bir karar üretmiyorsa gereksiz XAI problemi oluşturma.

---

## 8. Demo Sırasında Kırılabilecek Noktalar

Canlı demo açısından incele:

- Uygulama başlamıyor
- Veri yolu yanlış
- Dependency eksik
- Gerekli environment variable eksik
- Harici servis / AI çağrısı başarısız
- Uzun bekleme süresi
- Demo verisi beklenmeyen formatta
- Ekranda hata mesajı
- X-Factor yalnızca belirli bir inputta çalışıyor
- Sonuç tekrar üretilemiyor
- Gösterilen ekran gerçek ürün davranışıyla uyuşmuyor

Her risk için:
- Kırılma noktası
- Olası etki
- Nasıl test edilir?
- Demo öncesi minimum önlem

Sadece ilgili riskleri yaz.

---

## 9. En Kritik 5 Test

En yüksek bilgi ve risk azaltma değerine sahip en fazla 5 test öner.

Her test için:

### Test <N>

**Amaç:**
<neyi doğruluyor?>

**Girdi / Ön Koşul:**
<ne gerekiyor?>

**Adımlar:**
<kısa test akışı>

**Beklenen Sonuç:**
<doğru davranış>

**Başarısızlık Ne Anlama Gelir?**
<hangi problem ortaya çıkar?>

**Öncelik:**
KRİTİK / ORTA / DÜŞÜK

Testleri mümkün olduğunca:
- kabul kriterlerine,
- çekirdek çözüm akışına,
- X-Factor'a,
- demo risklerine

bağla.

---

## 10. Öncelikli Düzeltmeler

Bulguları düzeltme sırasına koy.

Tablo oluştur:

| Öncelik | Bulgu | Minimum Düzeltme | Tahmini Risk Azaltma | Demo Öncesi Gerekli mi? |
|---|---|---|---|---|
| 1 | ... | ... | Yüksek / Orta / Düşük | Evet / Hayır |

Öncelik sırası:

1. Çözümün yanlış sonuç üretmesine neden olan problemler
2. Çalışmayı veya demoyu engelleyen problemler
3. Kanıtsız / yanıltıcı çıktılar
4. Güvenlik ve veri problemleri
5. Daha düşük öncelikli kalite problemleri

Yeni özellik geliştirmeyi düzeltme olarak önermemeye çalış.

---

## 11. Final Red-Team Kararı

Aşağıdakilerden birini seç:

- DEMO İÇİN HAZIR
- KRİTİK DÜZELTME SONRASI HAZIR
- HENÜZ HAZIR DEĞİL
- MEVCUT KANITLA KARAR VERİLEMEZ

Ardından en fazla 3 cümleyle nedenini açıkla.

Bu kararın yalnızca verilen kanıt ve test sonuçlarına dayandığını belirt.

---

KURALLAR:
- Bir problem bulamadığında problem uydurma.
- Varsayım ile doğrulanmış hatayı ayır.
- Kanıt yoksa "DOĞRULAMA GEREKİYOR" yaz.
- Çalıştırılmamış testi geçmiş gibi gösterme.
- Kod görülmediyse kod hatası varmış gibi davranma.
- AI kullanılmıyorsa hallucination riski uydurma.
- Yeni özellik önermek yerine mevcut çözümün güvenilirliğine odaklan.
- Gereksiz production ölçeği problemi üretme.
- Ölçülmemiş sayı veya oran üretme.
- Küçük stil problemlerini kritik hata gibi sınıflandırma.
- Kritik seviyeyi gerçekten teslimi, doğruluğu, güvenliği veya demoyu ciddi etkileyen konular için kullan.