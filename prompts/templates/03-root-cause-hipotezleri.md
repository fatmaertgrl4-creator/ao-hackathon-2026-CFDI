ROL:
SRE incident investigation, observability, log / metric analizi ve
root-cause analysis konusunda deneyimli bir uzman gibi hareket et.

AMACIN:
Kesin root cause uydurmak değil;
mevcut kanıtlardan hareketle test edilebilir root cause hipotezleri üretmek,
bu hipotezleri birbirinden ayırmak ve en hızlı doğrulama yolunu önermek.

PROBLEM:
{{PROBLEM}}

DOĞRULANMIŞ BULGULAR:
{{BULGULAR}}

ÖLÇÜLEN METRİKLER:
{{METRIKLER}}

LOG / HATA / EXCEPTION ÖRNEKLERİ:
{{LOG_ORNEKLERI}}

VARSA EK BAĞLAM:
{{EK_BAGLAM}}

KISITLAR:
- Yalnızca verilen problem, doğrulanmış bulgular, metrikler ve logları kullan.
- Kesin root cause ilan etme.
- Veride olmayan servis, dependency, exception, olay veya zaman ilişkisi üretme.
- Korelasyonu nedensellik olarak sunma.
- Hipotezleri gerçekmiş gibi ifade etme.
- Yetersiz kanıt varsa bunu açıkça belirt.
- En fazla 5 hipotez üret.
- Hipotezleri kanıt gücüne göre güçlüden zayıfa sırala.

Çıktını aşağıdaki formatta üret:

## 1. Kanıta Dayalı Root Cause Hipotezleri

Her hipotez için:

### Hipotez <N>

**Hipotez:**
<test edilebilir ve mümkün olduğunca spesifik ifade>

**Destekleyen Kanıt:**
Yalnızca verilen bilgiler içerisindeki gerçek kanıtları kullan.

Her kanıt için mümkünse:
- Kanıt
- Kaynak / alan / log
- Hipotezi neden desteklediği

**Çelişen / Zayıflatan Kanıt:**
Hipoteze ters düşen veya güveni azaltan veri varsa belirt.

Yoksa:
"Verilen bilgiler içinde belirgin çelişen kanıt bulunamadı."

Ancak bunu hipotezin doğrulandığı anlamına getirme.

**Eksik Kanıt:**
Kesin sonuca yaklaşmak için hangi bilgi eksik?

**Doğrulama Testi:**
Hipotezi desteklemek veya elemek için yapılabilecek
en küçük, hızlı ve düşük maliyetli test nedir?

Mümkünse belirt:
- Kontrol edilecek veri
- Beklenen sonuç
- Hipotezi destekleyen sonuç
- Hipotezi zayıflatan sonuç

**Güven Seviyesi:**
Düşük / Orta / Yüksek

**Güven Gerekçesi:**
Bu güven seviyesini hangi kanıtlara dayanarak verdiğini açıkla.

Yeterli kanıt yoksa "Yüksek" güven verme.

---

## 2. Hipotezlerin Karşılaştırması

Kısa bir tablo oluştur:

| Sıra | Hipotez | Destek Gücü | Eksik Kanıt | Test Kolaylığı | Güven |
|---|---|---|---|---|---|
| 1 | ... | ... | ... | ... | ... |

Sıralamayı yalnızca kanıt gücüne göre yap;
daha ilgi çekici olduğu için bir hipotezi öne çıkarma.

---

## 3. En Güçlü Mevcut Hipotez

Bu bölümü aşağıdaki açıklanabilirlik formatıyla yaz:

### SONUÇ
Şu anda en güçlü görünen hipotezi yaz.

Bunu kesin root cause olarak ifade etme.

### NEDEN
Bu hipotezin neden diğerlerinden daha güçlü olduğunu açıkla.

### KANIT
Yalnızca verilen veri içerisindeki en güçlü gerçek kanıtları belirt.

### GÜVEN
Düşük / Orta / Yüksek

### BELİRSİZLİK
Henüz neyi bilmiyoruz?

### SONRAKİ KONTROL
Bu hipotezi doğrulamaya veya elemeye en fazla katkı sağlayacak
bir sonraki kontrol nedir?

---

## 4. Neden Henüz Kesin Root Cause Diyemiyoruz?

Eksik kanıtları ve alternatif açıklamaları açık şekilde belirt.

Eğer mevcut kanıt gerçekten yetersizse bunu doğrudan söyle:

"MEVCUT KANIT KESİN ROOT CAUSE İÇİN YETERSİZ."

---

## 5. İnsan Tarafından Kontrol Edilmesi Gereken Noktalar

Ekibin teknik olarak doğrulaması gereken noktaları öncelik sırasıyla yaz.

Her madde için:
- Ne kontrol edilmeli?
- Neden önemli?
- Hangi hipotezi etkiler?

En fazla 5 madde yaz.

KURALLAR:
- Korelasyonu nedensellik olarak yorumlama.
- Logda olmayan exception üretme.
- Var olmayan servis, dependency, bileşen veya olay uydurma.
- Ölçülmeyen sayı veya oran üretme.
- Zaman ilişkisi kanıtlanmadıysa olayları birbirine bağlama.
- "Aynı anda oldu" bilgisini tek başına root cause kanıtı sayma.
- Hipotezi doğrulanmış gerçek gibi sunma.
- Alternatif açıklamaları göz ardı etme.
- Yetersiz kanıt varsa açıkça "KANIT YETERSİZ" yaz.
- SONUÇ + NEDEN + KANIT bölümünde yalnızca sağlanan gerçek kanıtları kullan.