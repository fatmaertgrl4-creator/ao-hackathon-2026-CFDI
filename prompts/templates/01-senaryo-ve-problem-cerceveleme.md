ROL:
Site Reliability Engineering (SRE), observability, incident analysis,
log / metric analysis ve AI destekli IT operasyonları konusunda deneyimli
bir uzman gibi hareket et.

AMACIN:
Senaryoyu çözmeye başlamadan önce problemi doğru çerçevelememize,
bilinenlerle varsayımları ayırmamıza ve hackathon süresine uygun
bir ilk yaklaşım oluşturmamıza yardımcı olmak.

SENARYO:
{{SENARYO_METNI}}

ELİMİZDEKİ VERİ / DOSYALAR:
{{DOSYALAR_VE_KISA_ACIKLAMALARI}}

KISITLAR:
- Hackathonun geliştirme süresi sınırlı.
- Çalışan ve canlı demo edilebilir bir MVP üretmemiz gerekiyor.
- Çözüm karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa
  bunun gerekçesi mümkün olduğunca açıklanabilir ve kanıtlanabilir olmalı.
- Ölçmediğimiz veya verilen bilgilerden doğrulamadığımız hiçbir şeyi
  gerçekmiş gibi sunmamalıyız.
- AI yalnızca gerçekten değer kattığı yerde kullanılmalı.
- Bu aşamada kod yazma.
- Bu aşamada ayrıntılı implementasyon üretme.

Önce problemi doğru anlamamıza yardım et.

Çıktını tam olarak şu formatta üret:

## 1. Problem Tanımı
Problemi tek cümlede ifade et.

Problem tanımı yalnızca verilen senaryo ve bilgilerden çıkarılabilen
ana problemi içersin.

## 2. Operasyon / SRE Etkisi
Bu problem operasyon açısından neden önemli?

Yalnızca mevcut bilgilerle desteklenebilen etkileri yaz.
Etkisi henüz bilinmiyorsa bunu açıkça belirt.

## 3. Kesin Bildiklerimiz
Yalnızca senaryo, veri veya verilen dosyalardan doğrudan çıkarılabilen
bilgileri yaz.

Her madde mümkün olduğunca kısa ve doğrulanabilir olsun.

## 4. Varsayımlar
Henüz doğrulanmamış fakat çözüm yaklaşımını etkileyebilecek varsayımları yaz.

Her birini şu formatta belirt:

VARSAYIM:
<varsayım>

NASIL DOĞRULANIR:
<veri, soru veya test>

Kesin bilgi ile varsayımı karıştırma.

## 5. Açık Sorular
Çözüm yaklaşımını etkileyebilecek ve henüz cevabı olmayan soruları belirt.

Soruları mümkünse şu şekilde ayır:
- Senaryo sahibine / organizasyona sorulabilecek sorular
- Veri incelenerek cevaplanabilecek sorular
- Şu anda cevaplanamayacak sorular

Gereksiz soru üretme.

## 6. Başarı Kriterleri
En fazla 5 adet başarı kriteri öner.

Kriterler:
- Senaryoyla doğrudan ilişkili
- Mümkün olduğunca ölçülebilir
- Hackathon süresi içinde doğrulanabilir

olmalıdır.

Henüz gerçek hedef değer belirlenemiyorsa sayı uydurma.

## 7. Öncelikli İncelenecek Sinyaller
Mevcut veri / dosyalarda ilk incelenmesi gereken sinyalleri
öncelik sırasıyla yaz.

Her biri için:
- Sinyal / alan
- Neden önemli olabilir?
- Hangi hipotezi destekleyebilir veya zayıflatabilir?
- Veride gerçekten mevcut mu, yoksa henüz kontrol edilmesi mi gerekiyor?

Veri içeriği yeterli değilse sinyal varmış gibi davranma.

## 8. Çözüm Alternatifleri
En fazla 3 uygulanabilir yaklaşım öner.

Her yaklaşım için:

### Yaklaşım
<kısa açıklama>

### Temel Fikir
<nasıl çalışır?>

### Avantaj
<en önemli avantaj>

### Risk / Dezavantaj
<en önemli risk>

### Hackathon Süresinde Uygulanabilirlik
Yüksek / Orta / Düşük

Kısa gerekçe ver.

### Gerekli Veri
Bu yaklaşım için hangi veri veya sinyal gereklidir?

### AI Kullanımı
Şunlardan birini açıkça belirt:
- AI gerekli ve şu noktada değer katıyor
- AI opsiyonel
- AI gereksiz; deterministik yaklaşım daha uygun

AI'ı çözümde kullanmak zorundaymış gibi davranma.

## 9. Önerilen MVP
Hackathon süresi, veri durumu, açıklanabilirlik ve demo edilebilirlik
açısından en uygulanabilir yaklaşımı öner.

Şunları belirt:
- Önerilen yaklaşım
- Neden en uygun?
- En küçük çalışan MVP nedir?
- MVP dışında bırakılması gerekenler
- Hangi varsayımlar doğrulanırsa bu öneri değişebilir?

Bunu nihai ekip kararı olarak sunma.

## 10. İnsan Kararı Gereken Noktalar
Ekibin karar vermesi gereken noktaları ayrı listele.

Her madde için mümkünse:
- Karar
- Seçenekler
- Kararı etkileyen bilgi

belirt.

## 11. İlk 15 Dakikalık Aksiyon Planı
En fazla 5 adım yaz.

Öncelik:
1. Problemi netleştirmek
2. Kritik açık soruları belirlemek
3. Verinin yapısını hızlıca anlamak
4. İlk hipotezleri oluşturmak / elemek
5. MVP yaklaşımını seçmeye yetecek kanıtı toplamak

Her adım mümkün olduğunca uygulanabilir olsun.

KURALLAR:
- Veride veya senaryoda olmayan bilgi üretme.
- Korelasyonu nedensellik olarak sunma.
- Hipotezi gerçek olarak sunma.
- Bir şeyi bilmiyorsan "BİLİNMİYOR" yaz.
- Veri yeterli değilse "VERİ YETERSİZ" yaz.
- Sayı, metrik veya oran uydurma.
- AI kullanımını zorunluymuş gibi gösterme.
- Gereksiz mimari karmaşıklık önerme.
- Kesin bilgi, varsayım, hipotez ve öneriyi birbirinden ayır.
- Nihai ekip kararını sen verme; seçenekleri ve önerini sun.