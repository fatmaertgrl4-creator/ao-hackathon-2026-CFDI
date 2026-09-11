# Prompt'lar

Bu dizin, hackathon boyunca yapay zekânın **nerede, hangi amaçla, nasıl kullanıldığını ve AI çıktıları sonrasında hangi insan kararlarının verildiğini** belgelemek için kullanılır.

`AI_JURI.md` → **1. AI Stratejimiz ve İş Akışı** bölümünün önemli kanıt kaynaklarından biridir.

> **Önemli:** Bu klasörün amacı mümkün olduğunca fazla prompt saklamak değil,
> çözümün gelişimini gerçekten etkileyen AI kullanımlarını açık ve doğrulanabilir şekilde göstermektir.

---

## Dizin Yapısı

```text
prompts/
│
├── README.md
├── _SABLON.md
│
├── templates/
│   ├── 01-senaryo-ve-problem-cerceveleme.md
│   ├── 02-veri-kesfi.md
│   ├── 03-root-cause-hipotezleri.md
│   ├── 04-mvp-mimarisi.md
│   ├── 05-modul-gelistirme.md
│   ├── 06-xai-aciklama.md
│   ├── 07-x-factor-secimi.md
│   ├── 08-model-karsilastirma.md
│   ├── 09-red-team-test.md
│   ├── 10-final-dokumantasyon-auditi.md
│   └── 11-demo-ve-sunum.md
│
└── used/
    └── yarışma sırasında gerçekten kullanılan kritik prompt kayıtları
```

---

## `templates/` Nedir?

`templates/` klasörü, senaryo açıklanmadan önce hazırlanmış **genel amaçlı ve tekrar kullanılabilir prompt şablonlarını** içerir.

Bu şablonlar:

- Senaryoya özel çözüm içermez
- Gerçek problem sonucunu önceden varsaymaz
- Gerçek metrik veya bulgu içermez
- Yarışma sırasında gerçek bağlamla doldurulmak üzere hazırlanmıştır

Yarışma sırasında ihtiyaç halinde:

- Gerçek senaryo
- Gerçek veri yapısı
- Doğrulanmış bulgular
- Gerçek kısıtlar
- Gerçek kararlar

ile uyarlanarak kullanılabilir.

> **Önemli:** Bir prompt şablonunun repository'de bulunması,
> o prompt'un yarışma sırasında gerçekten kullanıldığı anlamına gelmez.

Template'ler **hazırlık aracıdır**; gerçek AI kullanım kanıtı değildir.

---

## `used/` Nedir?

`used/` klasörü, hackathon sırasında **gerçekten kullanılan ve çözüm sürecine anlamlı katkı sağlayan kritik prompt kayıtlarını** içerir.

AI kullanım stratejisinin gerçek çalışma izi burada tutulur.

Her kayıt mümkün olduğunca aşağıdaki bilgileri içermelidir:

- Prompt'un amacı
- Kullanılan araç / platform
- Model adı
- Model sürümü
- Kullanıldığı tarih / faz
- Prompt'un bağlamı
- Gerçek prompt metni
- Model çıktısının önemli özeti
- Ekibin verdiği karar
- Yapılan doğrulama
- İlgili gerçek repository kanıtı
- Çözüm üzerindeki etkisi

Kayıt formatı için:

[`_SABLON.md`](_SABLON.md)

> **Önemli:** Model adı veya sürümü tahmin edilmemelidir.
> Doğrulanamayan bilgi gerçekmiş gibi yazılmamalıdır.

---

## Hangi Prompt'lar Kaydedilmeli?

Her AI mesajını repository'ye eklemek gerekli değildir.

Çözümün yönünü, geliştirilmesini, doğrulanmasını veya açıklanmasını gerçekten etkileyen kritik kullanımlara öncelik verilmelidir.

Örnek kullanım türleri:

- Senaryoyu ve problemi çerçeveleyen prompt'lar
- Veri yapısını ve önemli sinyalleri inceleyen prompt'lar
- Hipotez oluşturan veya değerlendiren analizler
- Mimari / tasarım kararlarını etkileyen prompt'lar
- Kritik bir modülün geliştirilmesine katkı sağlayan prompt'lar
- Önemli bir hatanın çözümüne yardımcı olan debug prompt'ları
- Açıklanabilirlik / XAI çıktısını geliştiren prompt'lar
- X-Factor alternatiflerini değerlendiren prompt'lar
- Gerçekten yapılan model karşılaştırmaları
- Test / red-team kontrolleri
- Final dokümantasyon ve tutarlılık kontrolleri
- Demo / sunum hazırlığını anlamlı şekilde etkileyen prompt'lar

> Senaryoda root-cause analizi gerekmiyorsa sırf template bulunduğu için root-cause prompt'u kullanmak veya kaydetmek gerekli değildir.

---

## Başarısız veya Reddedilen Prompt'lar da Değerli Olabilir

Her kaydedilen prompt'un başarılı olması gerekmez.

AI önerisi ekip tarafından değerlendirilmiş ve bu değerlendirme çözüm yönünü değiştirmişse,
reddedilen bir öneri de gerçek çalışma sürecinin anlamlı kanıtı olabilir.

Örnek yapı:

```text
AI önerisi:
TODO — Modelin gerçek önerisinin kısa özeti

İnsan değerlendirmesi:
TODO — Ekip öneriyi neden kabul etti, değiştirdi veya reddetti?

Sonuç:
TODO — Bu karar çözüm yaklaşımını nasıl etkiledi?
```

Bu tür kayıtlar şu akışı görünür hale getirir:

```text
AI önerdi
    ↓
İnsan değerlendirdi
    ↓
Kabul / değişiklik / ret kararı verildi
    ↓
Sonuç doğrulandı
```

> **Önemli:** Gerçekte yapılmamış bir deneme sonradan yapılmış gibi yazılmamalıdır.
> Prompt geçmişi yeniden oluşturulup orijinal etkileşimmiş gibi sunulmamalıdır.

---

## Dosya Adlandırma

Gerçek kullanım kayıtları için önerilen biçim:

```text
NN-kisa-aciklama.md
```

Örnek:

```text
used/
├── 01-senaryo-analizi.md
├── 02-veri-kesfi.md
├── 03-hipotez-degerlendirmesi.md
├── 04-mimari-karari.md
├── 05-modul-gelistirme.md
├── 06-xai-aciklamasi.md
└── 07-model-karsilastirmasi.md
```

Numaralandırma, AI kullanım sürecinin yaklaşık sırasını takip etmeyi kolaylaştırır.

Dosya adları gerçek kullanım amacını yansıtmalıdır.

---

## Her Prompt İçin Kanıt

Bir prompt çözüm üzerinde gerçek bir değişikliğe, karara veya çıktıya yol açtıysa mümkün olduğunda ilgili repository kanıtı belirtilmelidir.

Örnek:

```text
src/<gercek_dosya>
```

veya:

```text
docs/mimari.md
```

veya:

```text
demo/<gercek_kanit>
```

X-Factor ile doğrudan ilişkili bir kullanım varsa, gerekli olduğunda gerçek kod yolu ve satır aralığı belirtilebilir:

```text
src/<gercek_dosya>:<gercek_satir_araligi>
```

> **Önemli:** Var olmayan dosya, özellik, çıktı veya satır aralığı referans olarak verilmemelidir.
>
> Satır numarası kullanılan kanıtlar final kod değişikliklerinden sonra yeniden doğrulanmalıdır.

---

## İnsan – AI İş Bölümü

Her kritik prompt kaydında yalnızca modelin ne yaptığı değil,
**ekibin AI çıktısı karşısında ne yaptığı** da gösterilmelidir.

Örnek yapı:

```text
AI:
Alternatif çözüm yaklaşımları önerdi.

İnsan:
Senaryo, süre ve veri kısıtlarına göre uygun yaklaşımı seçti.

Doğrulama:
Seçilen yaklaşım gerçek veri veya çalışan çözüm üzerinde kontrol edildi.
```

Temel akış:

```text
AI çıktı üretti
        ↓
İnsan değerlendirdi
        ↓
Karar verdi
        ↓
Sonuç doğrulandı
```

AI çıktısı tek başına doğrulanmış gerçek veya kanıt olarak kabul edilmemelidir.

---

## Doğrulama

Kritik AI çıktıları mümkün olduğunda doğrulanmalıdır.

Doğrulama yöntemi kullanım türüne göre değişebilir.

Örnekler:

- Gerçek veri ile karşılaştırma
- Kodun çalıştırılması
- Test sonucu
- Hesaplanan metrik
- Dosya / çıktı kontrolü
- Alternatif yaklaşım karşılaştırması
- İnsan teknik incelemesi

Prompt kaydında:

```text
Doğrulama:
TODO
```

şeklinde kullanılan gerçek yöntem belirtilmelidir.

> “AI söyledi” bir doğrulama yöntemi değildir.

---

## Model Bilgileri

Her gerçek kullanım kaydında mümkün olduğunda aşağıdakiler belirtilmelidir:

- Platform / araç
- Model adı
- Model sürümü
- Kullanım amacı

Model adı veya sürümü tahmin edilmemelidir.

Doğrulanamayan model bilgisi gerçekmiş gibi final dokümana yazılmamalıdır.

Aynı görev için birden fazla model gerçekten karşılaştırıldıysa
bu karşılaştırma ayrıca belgelenebilir.

---

## Template ve Gerçek Kullanım Ayrımı

Aşağıdaki ayrım korunmalıdır:

```text
prompts/templates/
→ Yarışma öncesi hazırlanmış genel prompt şablonları

prompts/used/
→ Yarışma sırasında gerçekten kullanılan prompt kayıtları
```

Final dokümantasyonda:

> “Bu prompt'u kullandık.”

denebilmesi için ilgili kullanımın gerçekten gerçekleşmiş olması gerekir.

Bir template'in repository'de bulunması kullanım kanıtı değildir.

---

## Güvenlik ve Veri Kuralları

Bu dizindeki dosyalar public GitHub repository'sine commit edilebilir.

Bu nedenle prompt metinleri commit edilmeden önce mutlaka kontrol edilmelidir.

Repository'ye eklenmemesi gereken bilgiler:

- API key
- Access token
- Parola
- Credential
- Private key
- Secret
- Gizli connection string
- Gerçek müşteri verisi
- Production verisi
- Kişisel veri
- Hassas kurum içi bilgi

Hackathon çözümünde yalnızca etkinlik kapsamında izin verilen sentetik veriler kullanılmalıdır.

> Bir prompt içerisinde gizli veya hassas bilgi bulunuyorsa prompt olduğu gibi public repository'ye commit edilmemelidir.
>
> Hassas değeri maskeleyerek veya prompt'u güvenli şekilde yeniden düzenleyerek kayıt altına alın.

---

## Final Kontrolü

Teslimden önce:

- [ ] Kritik gerçek AI kullanımları `prompts/used/` altında kayıtlı
- [ ] Template'ler ve gerçek kullanım kayıtları açık şekilde ayrılmış
- [ ] Kullanılan araç / platform bilgileri doğru
- [ ] Model adları doğrulanmış
- [ ] Model sürümleri doğrulanmış
- [ ] Gerçek prompt metinleri doğru
- [ ] Model çıktısı özeti gerçek kullanımla uyumlu
- [ ] İnsan kararları belirtilmiş
- [ ] Doğrulama adımları belirtilmiş
- [ ] Repository kanıtları gerçek
- [ ] X-Factor ile ilgili kullanım varsa gerçek kanıtla bağlantılı
- [ ] Satır referansları final kodla doğrulanmış
- [ ] Kullanılmamış template'ler gerçek kullanım gibi gösterilmiyor
- [ ] Sonradan uydurulmuş prompt geçmişi bulunmuyor
- [ ] Gizli bilgi bulunmuyor
- [ ] Gerçek müşteri / production / kişisel veri bulunmuyor

---

## Temel Prensip

Bu klasörün amacı yalnızca:

> **“AI kullandık.”**

demek değildir.

Amaç şunu kanıtlayabilmektir:

> **“AI'ı bu problemde, bu amaçla kullandık.
> Bu çıktıyı aldık.
> Ekip çıktıyı değerlendirdi ve bu kararı verdi.
> Sonucu bu yöntemle doğruladık.
> Bunun çözümdeki gerçek karşılığı da burada.”**

AI kullanımının değeri, kullanılan prompt sayısıyla değil;
**probleme sağladığı katkı, insan kararı, doğrulama ve gerçek kanıtla** gösterilmelidir.