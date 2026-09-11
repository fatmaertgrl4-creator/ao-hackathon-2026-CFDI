# Mimari

> **Durum: TASLAK**
>
> Bu doküman çözümün teknik mimarisini, ana bileşenlerini, veri ve karar akışını,
> harici bağımlılıklarını ve önemli teknik kararlarını açıklamak için kullanılacaktır.
>
> Senaryo henüz açıklanmadığı için çözüme özel alanlar `TODO` olarak bırakılmıştır.
> Senaryo ve veri paketi paylaşılıp çözüm geliştirildikten sonra bu alanlar yalnızca
> gerçek bileşenler, gerçek dosya yolları ve gerçekten kullanılan teknolojilerle güncellenecektir.
>
> Bu dosya `AI_JURI.md` → **2. Problemi Nasıl Çözdük** bölümündeki
> teknik yaklaşım ve çözüm mimarisi için kanıt olarak kullanılabilir.

---

## 1. Genel Mimari

TODO — Çözümün uçtan uca nasıl çalıştığını kısa ve anlaşılır şekilde açıklayın.

Aşağıdaki sorular cevaplanmalıdır:

- Veri veya kullanıcı girdisi sisteme nasıl giriyor?
- İlk olarak hangi bileşen tarafından işleniyor?
- İşleme / analiz / karar akışı hangi aşamalardan geçiyor?
- AI / LLM kullanılıyorsa hangi noktada ve hangi amaçla devreye giriyor?
- Sonuç nasıl oluşturuluyor?
- Sonuç nasıl doğrulanıyor?
- Kullanıcı çıktıyı nerede veya hangi formatta görüyor?

> **Önemli:** Mimari anlatımı yalnızca teknoloji isimlerinden oluşmamalıdır.
> Verinin, kararların ve çıktının sistem içerisinde nasıl ilerlediği anlaşılmalıdır.
>
> Final durumda yalnızca gerçekten geliştirilmiş akış anlatılmalıdır.

---

## 2. Veri ve Karar Akışı

TODO — Gerçek çözüm oluşturulduktan sonra aşağıdaki şema gerçek mimariye göre güncellenecektir.

Başlangıç şablonu:

```text
[ Veri / Kullanıcı Girdisi ]
            |
            v
[ Girdi Doğrulama / Hazırlama ]
            |
            v
[ Temel İşleme / Analiz ]
            |
            v
[ Karar / Değerlendirme Katmanı ]
            |
            v
[ Doğrulama / Kanıt ]
            |
            v
[ Kullanıcı Çıktısı ]
```

AI gerçekten kullanılıyorsa ilgili noktaya ayrıca eklenebilir:

```text
[ Hazırlanmış Bağlam / Sinyaller ]
              |
              v
[ AI / LLM ]
              |
              v
[ Yapılandırılmış Çıktı ]
              |
              v
[ Doğrulama / Kontrol ]
```

> **Not:** Bu şemalar yalnızca başlangıç şablonudur.
> Kullanılmayan adımlar kaldırılmalı, gerçek çözümde bulunan bileşenler eklenmelidir.
>
> AI kullanılmayan bir aşama sırf mimaride AI görünsün diye eklenmemelidir.

---

## 3. Bileşenler

Her ana bileşen için sorumluluk, gerçek kod konumu, girdi ve çıktı belirtilmelidir.

### 3.1. TODO — Bileşen Adı

**Sorumluluk:**  
TODO — Bu bileşen ne yapıyor?

**Kod Konumu:**  
`src/TODO`

**Girdi:**  
TODO

**Çıktı:**  
TODO

**Bağımlılıklar:**  
TODO

**AI Kullanımı:**  
TODO — AI kullanılıyor mu? Kullanılıyorsa hangi somut görev için?

**Doğrulama:**  
TODO — Bu bileşenin doğru çalıştığı nasıl doğrulanıyor?

---

### 3.2. TODO — Bileşen Adı

**Sorumluluk:**  
TODO

**Kod Konumu:**  
`src/TODO`

**Girdi:**  
TODO

**Çıktı:**  
TODO

**Bağımlılıklar:**  
TODO

**AI Kullanımı:**  
TODO

**Doğrulama:**  
TODO

---

> **Önemli:** Final teslimde yalnızca gerçekten var olan bileşenler yazılmalıdır.
> Dosya yolları final repository üzerinden doğrulanmalıdır.

---

## 4. AI / LLM Entegrasyonu

TODO — AI / LLM gerçekten kullanılıyorsa mimari içerisindeki görevi açıklanacaktır.

Aşağıdaki bilgiler mümkün olduğunca net verilmelidir:

- AI hangi bileşen veya aşamada çağrılıyor?
- AI'a hangi veri veya bağlam gönderiliyor?
- Ham veri mi, özetlenmiş veri mi gönderiliyor?
- Modelden hangi tür çıktı bekleniyor?
- Çıktı yapılandırılmış bir formatta mı alınıyor?
- Model çıktısı doğrudan mı kullanılıyor?
- Çıktı üzerinde doğrulama veya kontrol yapılıyor mu?
- Nihai karar AI, insan, deterministik kod veya bunların kombinasyonu tarafından mı oluşturuluyor?
- Hatalı / eksik AI çıktısı nasıl ele alınıyor?
- Açıklanabilirlik gerekiyorsa nasıl sağlanıyor?

Örnek mimari desen:

```text
[ Doğrulanmış Veri / Analiz Sonucu ]
                  |
                  v
[ Prompt / Context Hazırlama ]
                  |
                  v
[ AI / LLM ]
                  |
                  v
[ Yapılandırılmış Yanıt ]
                  |
                  v
[ Doğrulama / Kontrol ]
                  |
                  v
[ Kullanılabilir Sonuç ]
```

> **Önemli:** “LLM kullanıldı” tek başına yeterli değildir.
> Modelin hangi gerçek görevi üstlendiği ve çıktısının nasıl doğrulandığı açıklanmalıdır.
>
> AI / LLM çözümün mimarisinde kullanılmıyorsa bu bölümde açıkça belirtilmelidir.

---

## 5. Açıklanabilirlik — XAI Akışı

TODO — Çözüm bir karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa
bu sonucun kullanıcıya nasıl açıklandığı belirtilecektir.

Temel yaklaşım:

```text
SONUÇ
  +
NEDEN
  +
KANIT
```

Gerekli olduğunda daha ayrıntılı yapı:

```text
RESULT
  |
REASON
  |
EVIDENCE
  |
CONFIDENCE / UNCERTAINTY
  |
NEXT CHECK
```

Örnek yaklaşım:

```text
Sonuç:
Belirli bir kayıt veya bileşen öncelikli olarak değerlendirildi.

Neden:
Analiz sırasında ilgili kriterlerde anlamlı bir değişim gözlemlendi.

Kanıt:
Sonucu destekleyen gerçek ölçüm veya veri noktaları gösterildi.
```

> **Önemli:** Final örnekleri yalnızca gerçek veriye ve gerçekten üretilen sinyallere dayanmalıdır.
> Model tarafından üretilen fakat kanıtlanamayan gerekçeler kullanılmamalıdır.
> Korelasyon doğrudan nedensellik olarak sunulmamalıdır.

---

## 6. Veri Modeli

TODO — Çözümde gerçekten kullanılan temel veri yapıları açıklanacaktır.

| Varlık / Veri | Açıklama | Kaynak | Önemli Alanlar |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

Varsa veri ilişkileri:

```text
TODO
```

### Veri Kalitesi

Gerekliyse aşağıdaki konular açıklanabilir:

- Eksik değerler
- Geçersiz alanlar
- Veri tipi problemleri
- Zaman alanlarının tutarlılığı
- Tekrarlayan kayıtlar
- Veri kapsamının sınırları

> **Not:** Karmaşık bir veri modeli yoksa bu bölüm kısa tutulabilir.
> Gerçekte bulunmayan tablo, alan veya varlık eklenmemelidir.

---

## 7. Girdiler ve Çıktılar

### Girdiler

TODO — Sistemin gerçekten aldığı girdiler açıklanacaktır.

Örnek olabilecek formatlar:

- CSV
- JSON
- Log kayıtları
- Metrik verileri
- Olay / event kayıtları
- Kullanıcı girdisi

**Veri Yolu:**  
`TODO`

> **Not:** Final veri yolu `submission.json` → `calistirma.veri_yolu` alanı ile uyumlu olmalıdır.

### Çıktılar

TODO — Sistemin gerçekten ürettiği çıktılar açıklanacaktır.

Örnek olabilecek çıktı türleri:

- Analiz sonucu
- Önceliklendirilmiş kayıtlar
- Hipotez
- Açıklama
- Öneri
- Rapor
- Görselleştirme
- Web arayüzü
- Yapılandırılmış JSON çıktısı

> Final durumda yalnızca gerçekten üretilen çıktılar bırakılmalıdır.

---

## 8. Harici Bağımlılıklar

| Servis / Araç | Kullanım Amacı | Kimlik Doğrulama | Yapılandırma |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

Harici bağımlılık yoksa final durumda:

> Bu çözümde harici servis bağımlılığı bulunmamaktadır.

AI platformu veya başka bir dış servis kullanılıyorsa gerçek kullanım burada belirtilmelidir.

> **Önemli:** API key, token, parola, connection string veya gerçek credential değerleri
> bu dosyaya yazılmamalıdır.
>
> Gerekli yapılandırmalar yalnızca değişken isimleri üzerinden açıklanmalıdır.
> Gerçek gizli değerler repository içerisinde tutulmamalıdır.

---

## 9. Kullanılan Teknolojiler

| Teknoloji / Araç | Kullanım Amacı |
|---|---|
| TODO | TODO |
| TODO | TODO |

Gerekirse aşağıdaki kategoriler kullanılabilir:

- Programlama dili
- Veri işleme kütüphanesi
- Arayüz framework'ü
- AI / LLM platformu
- Test araçları
- Görselleştirme araçları

> **Not:** Finalde yalnızca gerçekten kullanılan teknoloji ve araçlar yazılmalıdır.
> Kullanılmayan bir teknoloji çözümün parçasıymış gibi gösterilmemelidir.

---

## 10. Kritik Teknik Kararlar

Çözüm geliştirilirken verilen önemli teknik kararlar ve bu kararların nedenleri burada tutulacaktır.

| Karar | Değerlendirilen Alternatif | Neden Bu Seçildi? | Kanıt / Sonuç |
|---|---|---|---|
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

Örnek karar türü:

```text
Karar:
Önce deterministik işlemlerle gerekli sinyalleri üretmek,
AI'a yalnızca ihtiyaç duyduğu bağlamı göndermek.

Alternatif:
Tüm girdiyi doğrudan modele göndermek.

Neden:
Daha kontrollü, tekrarlanabilir ve doğrulanabilir bir akış elde etmek.
```

> **Not:** Bu yalnızca bir örnektir.
> Final dokümanda yalnızca gerçekten alınan teknik kararlar bulunmalıdır.
>
> Sadece “ne seçtik?” değil, “neden seçtik?” sorusu da cevaplanmalıdır.

---

## 11. Hata Yönetimi ve Güvenli Davranış

TODO — Uygulamanın gerçekten ele aldığı hata durumları ve davranışları açıklanacaktır.

Kontrol edilebilecek durumlara örnek:

- Girdi dosyası bulunamazsa
- Veri okunamazsa
- Beklenen alan bulunmazsa
- Veri boşsa
- Geçersiz veri formatı gelirse
- AI çağrısı başarısız olursa
- AI beklenen formatta cevap vermezse
- Harici servis erişilemezse
- Beklenmeyen uygulama hatası oluşursa

Her gerçek hata durumu için mümkünse:

- Sistem ne yapıyor?
- Kullanıcıya ne gösteriyor?
- İşlem güvenli şekilde duruyor mu?
- Fallback davranışı var mı?

açıklanmalıdır.

> **Önemli:** Final dokümana yalnızca uygulamada gerçekten ele alınan hata durumları yazılmalıdır.

---

## 12. Doğrulama ve Test Yaklaşımı

TODO — Mimari ve çözüm çıktılarının nasıl doğrulandığı açıklanacaktır.

Gerekirse aşağıdakiler belirtilebilir:

- Modül testleri
- Uçtan uca test
- Örnek veri ile doğrulama
- Edge case testleri
- AI çıktılarının veri ile karşılaştırılması
- Beklenen / gerçekleşen çıktı kontrolü
- Manuel insan doğrulaması

| Kontrol | Yöntem | Sonuç |
|---|---|---|
| TODO | TODO | TODO |
| TODO | TODO | TODO |

> **Önemli:** “Test edildi” ifadesi mümkün olduğunda hangi yöntemle test edildiğiyle birlikte yazılmalıdır.

---

## 13. Bilinen Mimari Sınırlar

TODO — Mimari açıdan bilinçli olarak yapılamayan, sınırlı kalan
veya süre nedeniyle kapsam dışında bırakılan noktalar belirtilecektir.

| Sınır | Nedeni | Etkisi | Nasıl Geliştirilebilir? |
|---|---|---|---|
| TODO | TODO | TODO | TODO |

> Bilinen sınırlar gerçek çözümle uyumlu olmalı ve çözüm olduğundan daha kapsamlı gösterilmemelidir.

---

## 14. Kod Haritası

Finalde mimaride anlatılan ana bileşenlerin gerçek kod karşılıkları buraya eklenecektir.

| Bileşen | Dosya / Konum | Açıklama |
|---|---|---|
| TODO | `src/TODO` | TODO |
| TODO | `src/TODO` | TODO |
| TODO | `src/TODO` | TODO |

### X-Factor Kanıtı

X-Factor için gerçek kod konumu:

```text
src/<gerçek_dosya_adı>:<gerçek_satır_aralığı>
```

> **Önemli:** Buradaki tüm dosya yolları final repository içerisinde gerçekten bulunmalıdır.
> Satır referansları final commit sonrasında yeniden doğrulanmalıdır.

---

## 15. Mimari Tutarlılık Kontrolü

Final teslimden önce:

- [ ] Mimari gerçek çalışan çözümü anlatıyor
- [ ] Kullanılmayan bileşenler dokümandan kaldırıldı
- [ ] Gerçek kod yolları doğrulandı
- [ ] Veri yolu `submission.json` ile uyumlu
- [ ] AI / LLM kullanımı gerçek implementasyonla uyumlu
- [ ] Harici bağımlılıklar gerçek kullanım ile uyumlu
- [ ] Gizli erişim bilgisi bulunmuyor
- [ ] XAI anlatımı gerçek çıktı ile uyumlu
- [ ] X-Factor kanıt yolu doğrulandı
- [ ] Test ve doğrulama yöntemleri gerçek
- [ ] Bilinen sınırlar güncel
- [ ] Var olmayan teknoloji, bileşen veya özellik anlatılmıyor