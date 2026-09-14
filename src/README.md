# src/

Bu dizin projenin **kaynak kodunu** içerir.

> **Durum: TASLAK**
>
> Senaryo henüz açıklanmadığı için kaynak kod yapısı kesinleşmemiştir.
> Gerçek geliştirme başladığında bu dosya yalnızca gerçekten kullanılan
> modüller, giriş noktası, çalıştırma yöntemi ve temel kod yapısıyla güncellenecektir.
>
> Senaryoya özel olmayan genel yardımcı kodlar hazırlanmışsa bunlar açıkça
> gerçek çözüm bileşenlerinden ayrılmalıdır.

`src/`, özellikle `AI_JURI.md` içerisindeki:

- **2. Problemi Nasıl Çözdük**
- **3. X-Factor**

bölümlerindeki teknik iddialar için önemli kod kanıtlarından biridir.

X-Factor veya başka önemli bir teknik özellik için final teslimde gerçek
implementasyona gerektiğinde aşağıdaki biçimde referans verilebilir:

```text
src/<gercek_dosya>:<gercek_satir_araligi>
```

> **Önemli:** Final dokümantasyonda yalnızca gerçekten var olan dosyalar,
> gerçekten uygulanmış özellikler ve final kod üzerinden doğrulanmış satır
> aralıkları kullanılmalıdır.

---

## 1. Kaynak Kod Yapısı

TODO — Gerçek kod yapısı geliştirme sırasında burada gösterilecektir.

Örnek şablon:

```text
src/
├── README.md
├── <giris_noktasi>
├── <modul_1>
├── <modul_2>
└── ...
```

> Bu yalnızca biçim örneğidir.
> Finalde gerçek repository yapısı yazılmalı ve kullanılmayan örnekler kaldırılmalıdır.

Her ana dosyanın veya modülün çözüm içerisindeki görevi anlaşılır olmalıdır.

---

## 2. Giriş Noktası ve Çalıştırma

**Uygulamanın ana giriş noktası:**

```text
TODO
```

**Çalıştırma komutu:**

```bash
TODO
```

**Beklenen temel davranış / çıktı:**

TODO

> **ÇOK ÖNEMLİ:** Final çalıştırma komutu ilgili tüm dokümanlarda aynı olmalıdır.
>
> Özellikle:
>
> - Ana `README.md`
> - `AI_JURI.md` → Bölüm 4
> - `submission.json` → `calistirma.komut`
> - Bu `src/README.md`
>
> dosyaları arasında farklı çalıştırma komutları bırakılmamalıdır.

Komut final teslimden önce gerçekten çalıştırılarak doğrulanmalıdır.

---

## 3. Ana Modüller

Gerçek geliştirme başladığında çözümün ana modülleri burada kısa şekilde açıklanacaktır.

| Modül / Bileşen | Dosya / Konum | Sorumluluk | Doğrulama |
|---|---|---|---|
| TODO | `src/TODO` | TODO | TODO |
| TODO | `src/TODO` | TODO | TODO |
| TODO | `src/TODO` | TODO | TODO |

> Ayrıntılı veri ve karar akışı için:
> [`../docs/mimari.md`](../docs/mimari.md)

Final dokümanda yalnızca gerçekten var olan modüller bulunmalıdır.

---

## 4. AI / LLM Kullanılan Kod

AI / LLM çözümün çalışan uygulamasında gerçekten kullanılıyorsa,
ilgili kod konumları ve görevleri burada belirtilmelidir.

| Kullanım | Dosya / Konum | AI'ın Görevi | Çıktı Nasıl Doğrulanıyor? |
|---|---|---|---|
| TODO | `src/TODO` | TODO | TODO |

Açıklamada mümkün olduğunca şu sorular cevaplanmalıdır:

- AI hangi noktada devreye giriyor?
- AI'a hangi bağlam gönderiliyor?
- Modelden ne bekleniyor?
- Model çıktısı doğrudan mı kullanılıyor?
- Çıktı nasıl kontrol veya doğrulama sürecinden geçiyor?

> **Önemli:** “AI kullanıldı” şeklinde genel bir ifade yeterli değildir.
> Modelin çalışan çözüm içerisinde hangi gerçek görevi üstlendiği gösterilmelidir.
>
> Çalışan uygulamada AI / LLM entegrasyonu bulunmuyorsa bu bölümde açıkça
> belirtilmeli; var olmayan bir entegrasyon eklenmemelidir.

---

## 5. X-Factor Kod Kanıtı

Finalde seçilen ana X-Factor burada gerçek implementasyonuyla eşleştirilecektir.

**X-Factor:**

TODO

**Neden ayırt edici / değerli:**

TODO

**Ana kod kanıtı:**

```text
src/<gercek_dosya>:<gercek_satir_araligi>
```

X-Factor birden fazla bileşene yayılıyorsa ek gerçek kanıtlar da belirtilebilir:

```text
src/<gercek_dosya_1>:<satir_araligi>
src/<gercek_dosya_2>:<satir_araligi>
```

**Çalıştığını gösteren çıktı / demo kanıtı:**

```text
TODO
```

Bu bölüm:

- `AI_JURI.md` → Bölüm 3
- Ana `README.md` → X-Factor
- `submission.json` → `cozum.x_factor`
- Gerekliyse `demo/`

ile anlam bakımından tutarlı olmalıdır.

> **ÇOK ÖNEMLİ:** Dosya yolu veya satır numarası tahmin edilmemelidir.
> Satır referansları final kod değişiklikleri tamamlandıktan sonra yeniden doğrulanmalıdır.
>
> Kodun var olması tek başına yeterli değildir; mümkün olduğunda özelliğin gerçekten
> çalıştığını gösteren çıktı veya demo kanıtı da bulunmalıdır.

---

## 6. Bağımlılıklar

Çözüm dış paket veya kütüphane kullanıyorsa gerekli bağımlılıklar
tekrar kurulabilecek şekilde tanımlanmalıdır.

Kullanılan teknolojiye göre örnek dosyalar:

```text
requirements.txt
pyproject.toml
package.json
```

**Finalde kullanılan gerçek bağımlılık dosyası / yöntemi:**

```text
TODO
```

Bağımlılık dosyası gerekmiyorsa:

```text
Harici paket bağımlılığı bulunmamaktadır.
```

şeklinde açıkça belirtilebilir.

> **Önemli:** Kullanılmayan dependency dosyaları sırf şablonda bulunduğu için oluşturulmamalıdır.
>
> Ana README'deki kurulum adımları final teslimden önce gerçek ortamda test edilmelidir.

---

## 7. Ortam Değişkenleri ve Gizli Bilgiler

Kaynak kod ve repository içerisinde aşağıdaki hassas bilgiler bulunmamalıdır:

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

Çözüm ortam değişkeni kullanıyorsa gerçek değerler repository'ye yazılmamalıdır.

Yeni bir ortam değişkeni kullanıldığında gerekli değişken adı:

```text
.env.example
```

dosyasına güvenli biçimde eklenmelidir.

Gerçek değerler yalnızca güvenli yerel yapılandırmada tutulmalıdır.

> **Önemli:** Gerçek `.env` dosyası repository'ye commit edilmemelidir.
>
> Çözüm ortam değişkeni kullanmıyorsa yalnızca şablonu doldurmak amacıyla
> gereksiz değişken oluşturulmamalıdır.

---

## 8. Hata Yönetimi

Gerçek uygulamada ele alınan önemli hata durumları burada özetlenebilir.

| Hata / Durum | Sistem Davranışı | Kullanıcıya Gösterilen Sonuç |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |

Örnek olarak değerlendirilebilecek durumlar:

- Girdi dosyasının bulunamaması
- Geçersiz veya beklenmeyen veri
- Eksik zorunlu alan
- Boş veri
- AI / harici servis hatası
- Beklenmeyen uygulama hatası

> Finalde yalnızca gerçekten kod içerisinde ele alınan hata davranışları yazılmalıdır.

---

## 9. Test ve Doğrulama

Kaynak kodun hangi yöntemlerle doğrulandığı burada özetlenecektir.

| Kontrol | Komut / Yöntem | Sonuç |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |

Doğrulama türleri gerçek çözüme göre şunları içerebilir:

- Modül çalıştırma
- Unit test
- Uçtan uca test
- Örnek veri testi
- Edge case testi
- Beklenen / gerçekleşen çıktı karşılaştırması
- Manuel teknik doğrulama

> “Test edildi” ifadesi, mümkün olduğunda gerçekten yapılan test veya
> çalıştırma yöntemiyle desteklenmelidir.
>
> Çalıştırılmamış bir test başarılıymış gibi gösterilmemelidir.

---

## 10. Kodlama ve Doğrulama Prensibi

Geliştirme sırasında temel çalışma şekli:

```text
Küçük kapsam belirle
        ↓
Kodu geliştir
        ↓
Çalıştır
        ↓
Çıktıyı doğrula
        ↓
Gerekirse test et
        ↓
Dokümantasyonu güncelle
        ↓
Anlamlı commit oluştur
```

Büyük ve doğrulanmamış kod bloklarını tek seferde eklemek yerine
küçük, anlaşılır ve test edilebilir değişiklikler tercih edilmelidir.

AI tarafından üretilen kod da çalıştırılmadan ve kontrol edilmeden
doğru kabul edilmemelidir.

---

## 11. Kod ve Dokümantasyon Tutarlılığı

Kod değiştiğinde aşağıdaki dokümanların etkilenip etkilenmediği kontrol edilmelidir:

- Ana `README.md`
- `AI_JURI.md`
- `submission.json`
- `docs/mimari.md`
- `docs/plan.md`
- `demo/`
- `prompts/used/`

Özellikle aşağıdakiler değiştiyse dokümantasyon yeniden kontrol edilmelidir:

- Giriş noktası
- Çalıştırma komutu
- Dosya yolları
- AI entegrasyonu
- X-Factor
- Çıktı formatı
- Metrikler
- Harici bağımlılıklar

Kod ile dokümantasyon birbirini çelişkili şekilde anlatmamalıdır.

---

## 12. Final Kontrolü

Teslimden önce:

- [ ] Gerçek kaynak kod yapısı bu README'ye işlendi
- [ ] Ana giriş noktası gerçek
- [ ] Final çalıştırma komutu test edildi
- [ ] Çalıştırma komutu ilgili dokümanlarda tutarlı
- [ ] Beklenen temel çıktı doğru
- [ ] Ana modüller ve sorumlulukları gerçek kodla uyumlu
- [ ] AI / LLM kullanımı varsa gerçek kod konumu belirtildi
- [ ] AI çıktısının doğrulama yöntemi doğru
- [ ] X-Factor gerçek implementasyonla eşleştirildi
- [ ] X-Factor kod kanıtı gerçekten mevcut
- [ ] X-Factor satır aralıkları final kod üzerinden doğrulandı
- [ ] X-Factor'ın çalışan çıktı / demo kanıtı kontrol edildi
- [ ] Bağımlılık bilgileri güncel
- [ ] Gerçek test / doğrulama yöntemleri yazıldı
- [ ] `.env` commit edilmedi
- [ ] `.env.example` gerekiyorsa güncel
- [ ] Secret / credential bulunmuyor
- [ ] Gerçek müşteri / production / kişisel veri bulunmuyor
- [ ] `AI_JURI.md` içerisindeki kod referansları hâlâ geçerli
- [ ] `docs/mimari.md` gerçek kodu anlatıyor
- [ ] Var olmayan dosya, özellik veya sonuç anlatılmıyor
- [ ] Gerekli `TODO` alanları final bilgilerle güncellendi

---

## Mevcut Durum

Senaryo açıklanana kadar bu dizinde senaryoya özel bir çözüm varmış gibi
dokümantasyon oluşturulmamalıdır.

Hazırlık aşamasında yalnızca izin verilen genel ve tekrar kullanılabilir
yardımcı yapıların bulunması mümkündür.

Gerçek çözüm geliştirildikten sonra bu dosyadaki ilgili `TODO` alanları
gerçek kaynak kod, gerçek komutlar ve doğrulanmış kanıtlarla güncellenmelidir.