ROL:
SRE / observability sistemleri, incident analysis ve AI destekli
operasyon çözümleri tasarlama konusunda deneyimli bir solution architect
gibi hareket et.

AMACIN:
Üretim seviyesinde büyük veya karmaşık bir sistem tasarlamak değil;
hackathon süresi içinde geliştirilebilecek, çalışan, basit, test edilebilir,
açıklanabilir ve canlı demo edilebilir bir MVP mimarisi önermek.

PROBLEM:
{{PROBLEM}}

DOĞRULANMIŞ VERİ BULGULARI:
{{BULGULAR}}

SEÇİLEN YAKLAŞIM:
{{YAKLASIM}}

VARSA BAŞARI KRİTERLERİ:
{{BASARI_KRITERLERI}}

KALAN SÜRE:
{{KALAN_SURE}}

VARSA TEKNİK KISITLAR:
{{TEKNIK_KISITLAR}}

KISITLAR:
- Önce mimari öner; henüz final kod yazma.
- Yalnızca verilen problem, doğrulanmış bulgular ve seçilen yaklaşıma dayan.
- AI / LLM yalnızca gerçekten değer kattığı yerde kullanılmalı.
- Deterministik olarak daha güvenilir çözülebilecek işleri sırf AI kullanmak
  için LLM'e verme.
- Var olmayan servis, API, MCP, veri kaynağı veya entegrasyonu mevcutmuş gibi varsayma.
- Gereksiz mikroservis, dağıtık sistem veya production ölçeği karmaşıklığı önerme.
- Kalan süre içinde uygulanamayacak bileşenleri MVP'ye dahil etme.
- Önerdiğin dosya yolları yalnızca tasarım önerisidir;
  gerçekten oluşturulana kadar repository kanıtı değildir.

Çıktını aşağıdaki yapıda üret:

## 1. MVP'nin Temel Amacı

En fazla 3-4 cümleyle açıkla:

- MVP hangi problemi çözecek?
- Hangi girdiyi alacak?
- Hangi temel çıktıyı üretecek?
- Canlı demoda çalıştığını nasıl göstereceğiz?

MVP kapsamını gereksiz genişletme.

## 2. Uçtan Uca Veri ve Karar Akışı

Gerçek ihtiyaca göre uçtan uca akışı açıkla.

Örnek mantık:

Girdi
  ↓
Doğrulama / Hazırlama
  ↓
Deterministik İşleme / Analiz
  ↓
Karar veya Değerlendirme
  ↓
Doğrulama
  ↓
Çıktı

AI gerçekten gerekiyorsa ilgili noktaya ekle.

AI gerekmiyorsa akışa AI adımı ekleme.

Her aşama için:
- Girdi
- Yapılan işlem
- Çıktı
- Sonraki aşamaya neden gerekli olduğu

bilgisini kısa şekilde belirt.

## 3. Deterministik İşlemler

LLM kullanmadan kodla yapılması gereken işlemleri belirt.

Her biri için:
- İşlem
- Neden deterministik olmalı?
- Girdi
- Çıktı
- Nasıl doğrulanabilir?

Özellikle:
- hesaplamalar
- filtreleme
- aggregation
- veri doğrulama
- eşleştirme
- sıralama
- bilinen kurallar

gibi görevleri değerlendir.

AI'a verilmesi gerekmeyen işleri açıkça belirt.

## 4. AI / LLM'in Gerçek Görevi

Önce şu kararı ver:

AI DURUMU:
- Gerekli
- Opsiyonel
- Gereksiz

Kısa gerekçe yaz.

AI kullanılacaksa her görev için:
- AI ne yapıyor?
- Neden deterministik kod yerine AI uygun?
- AI'a hangi bağlam veriliyor?
- Hangi çıktı formatı bekleniyor?
- Çıktı sistem tarafından nasıl kullanılacak?
- AI hatası çözümü nasıl etkiler?

AI'ın kullanılmaması gereken görevleri de ayrıca belirt.

## 5. Doğrulama Katmanı

Sistem çıktılarının nasıl doğrulanacağını açıkla.

Aşağıdakileri gerekiyorsa ayrı değerlendir:
- Girdi doğrulama
- Veri kalitesi kontrolü
- Deterministik hesaplama doğrulaması
- AI çıktı formatı kontrolü
- AI çıktısının gerçek veriyle karşılaştırılması
- Beklenmeyen / eksik çıktı
- Hata veya fallback davranışı

Her kritik çıktı için:

ÇIKTI:
<çıktı>

DOĞRULAMA:
<nasıl kontrol edilir?>

BAŞARISIZLIK DURUMU:
<ne yapılır?>

AI çıktısını doğrulanmadan kesin gerçek olarak kullanma.

## 6. Açıklanabilirlik / XAI

Çözüm karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa
bunun nasıl açıklanacağını tasarla.

Temel yapı:

SONUÇ
+
NEDEN
+
KANIT

Gerekliyse:

GÜVEN / BELİRSİZLİK
+
SONRAKİ KONTROL

Her alan için verinin nereden geleceğini belirt.

Özellikle:
- SONUÇ ne tarafından üretiliyor?
- NEDEN hangi analizden geliyor?
- KANIT hangi gerçek veri veya metrikten geliyor?
- AI'ın kanıt uydurması nasıl engelleniyor?

Çözüm böyle bir karar üretmiyorsa gereksiz XAI katmanı tasarlama.

## 7. Önerilen Modüller

MVP için minimum sayıda modül öner.

Her modül için:

### Modül
<isim>

### Sorumluluk
<tek ana görev>

### Girdi
<girdi>

### Çıktı
<çıktı>

### AI Kullanıyor mu?
Evet / Hayır

Evet ise neden?

### Önerilen Kod Konumu
src/<onerilen_dosya>

### Doğrulama
Bu modülün doğru çalıştığı nasıl test edilir?

ÖNEMLİ:
Önerilen dosya adı henüz gerçek repository kanıtı değildir.
Dosya gerçekten oluşturulduğunda dokümantasyon gerçek yol ile güncellenmelidir.

Gereksiz katman veya modül üretme.

## 8. ASCII Mimari Şeması

Önerilen gerçek MVP akışını sade ASCII diyagramıyla göster.

Örneğin:

[ Girdi ]
    |
    v
[ Doğrulama ]
    |
    v
[ Analiz ]
    |
    +----> [ AI / LLM ]   <- yalnızca gerçekten gerekiyorsa
    |          |
    |          v
    +----> [ Doğrulama ]
               |
               v
           [ Çıktı ]

Gerçek önerine göre şemayı değiştir.

AI gerekmiyorsa AI kutusu ekleme.

## 9. Kritik Teknik Kararlar

En fazla 5 önemli karar yaz.

Her biri için:
- Karar
- Alternatif
- Neden bu seçenek?
- Süre / risk / açıklanabilirlik etkisi

Kararları hackathon şartlarına göre değerlendir.

## 10. Kritik Riskler

En fazla 5 gerçek risk yaz.

Her risk için:
- Risk
- Etki
- Olasılık: Düşük / Orta / Yüksek
- En küçük karşı önlem
- Demo üzerindeki etkisi

Teorik production riskleriyle listeyi gereksiz büyütme.

## 11. MVP Dışı Bırakılacaklar

Süre nedeniyle bilinçli olarak yapılmaması gereken özellikleri yaz.

Her biri için:
- Özellik
- Neden MVP dışında?
- Çekirdek çözüm onsuz çalışabilir mi?

"Nice to have" özellikleri çekirdek çözümden ayır.

## 12. Uygulama Sırası

Geliştirme sırasını en fazla 7 adım halinde öner.

Öncelik:
- Önce çalışan en küçük uçtan uca akış
- Sonra doğrulama
- Sonra gerekli AI entegrasyonu
- Sonra açıklanabilirlik
- Sonra X-Factor / iyileştirmeler

Her adım mümkün olduğunca tek başına test edilebilir olsun.

## 13. İnsan Kararı Gereken Noktalar

Ekibin karar vermesi gereken noktaları belirt.

Her biri için:
- Karar
- Seçenekler
- Önerin
- Kararı değiştirebilecek bilgi

Nihai kararı ekip adına verme.

KURALLAR:
- Gereksiz mikroservis veya karmaşık mimari önerme.
- Deterministik hesaplamaları sırf AI kullanmak için LLM'e verme.
- AI kullanımını zorunlu varsayma.
- Var olmayan entegrasyonları varsayma.
- Kanıtlanmamış özellikleri mimarinin mevcut parçası gibi anlatma.
- Kalan sürede uygulanamayacak mimari önerme.
- Güvenlik veya doğrulama katmanını tamamen atlama.
- Önerilen dosya yollarını gerçek repository kanıtı gibi sunma.
- Önce çalışan ve doğrulanabilir MVP'yi hedefle.