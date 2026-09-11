# Plan

> **Durum: TASLAK**
>
> Bu doküman hackathon boyunca problem çözme yaklaşımımızı, kapsamı,
> başarı kriterlerini, temel kararları ve çalışma planını takip etmek için kullanılacaktır.
>
> Senaryo henüz açıklanmadığı için çözüme özel alanlar `TODO` olarak bırakılmıştır.
> Senaryo ve veri paketi paylaşıldıktan sonra ilgili alanlar yalnızca gerçek bilgiler,
> doğrulanmış gözlemler ve alınan gerçek kararlarla güncellenecektir.
>
> Faz bazlı ilerleme takibi için: [`fazlar.md`](fazlar.md)

---

## 1. Hedef

TODO — Hackathon sonunda ortaya çıkarmak istediğimiz çözümü kısa ve somut şekilde açıklayın.

Aşağıdaki sorular cevaplanmalıdır:

- Hangi problemi çözüyoruz?
- Çözüm kim için değer üretiyor?
- Çözümün temel çıktısı nedir?
- AI çözüm içerisinde hangi gerçek rolü üstleniyor?
- Başarılı olduğumuzu nasıl anlayacağız?

> **Önemli:** “AI destekli bir uygulama geliştirmek” tek başına hedef değildir.
> Hedef, senaryoda verilen operasyon problemini ve çözümün üreteceği somut değeri açıklamalıdır.

---

## 2. Problem Tanımı

TODO — Senaryo açıklandıktan sonra problem kısa ve net şekilde tanımlanacaktır.

### Problem

TODO

### Operasyon / SRE Etkisi

TODO — Problemin operasyon açısından neden önemli olduğunu ve etkisini açıklayın.

### Beklenen Sonuç

TODO — Çözümün hangi temel sonucu üretmesi gerektiğini açıklayın.

### Açık Sorular

Senaryo veya veri incelendiğinde henüz cevaplanamayan önemli sorular:

- TODO
- TODO
- TODO

### Varsayımlar

Henüz doğrulanmamış varsayımlar:

- TODO
- TODO

> **Önemli:** Varsayımlar gerçek bilgi gibi sunulmamalıdır.
> Veri veya senaryo ile doğrulanan varsayımlar güncellenmeli;
> yanlışlananlar açıkça elenmelidir.

---

## 3. Kapsam

### Kapsam İçi

Bu hackathon kapsamında gerçekleştirilmesi planlanan işler:

- TODO
- TODO
- TODO

### Kapsam Dışı

Süre veya öncelik nedeniyle bilinçli olarak kapsam dışında bırakılan işler:

- TODO
- TODO

> **Önemli:** Kapsam, senaryo ve süre dikkate alınarak mümkün olduğunca küçük ve uygulanabilir tutulmalıdır.
>
> Final çözümde anlamlı bir kapsam dışı madde kaldıysa gerektiğinde
> `AI_JURI.md` → **Bilinen Sınırlar** bölümünde de belirtilmelidir.

---

## 4. Başarı Kriterleri

Çözümün tamamlandı sayılması için başarı kriterleri mümkün olduğunca ölçülebilir ve senaryoya özel olmalıdır.

| Kriter | Hedef | Ölçüm / Doğrulama Yöntemi | Durum |
|---|---|---|---|
| TODO | TODO | TODO | Beklemede |
| TODO | TODO | TODO | Beklemede |
| TODO | TODO | TODO | Beklemede |

Olası kriter türleri:

- Verinin başarıyla işlenebilmesi
- Senaryoda istenen temel çıktının üretilebilmesi
- Sonucun gerektiğinde gerekçesi ve kanıtıyla açıklanabilmesi
- Çözümün tanımlanan çalıştırma komutuyla başlatılabilmesi
- Demo akışının uçtan uca tamamlanabilmesi
- Senaryoya uygun en az bir ölçülebilir sonucun üretilebilmesi

> **Önemli:** Final başarı kriterleri senaryoya göre belirlenmelidir.
> Ölçülmeyen veya doğrulanmayan sonuçlar başarı kriteri gerçekleşmiş gibi gösterilmemelidir.

---

## 5. İlk Analiz ve Hipotezler

TODO — Senaryo ve veri paketi açıldıktan sonraki ilk incelemeler burada tutulacaktır.

### Veri Hakkında İlk Gözlemler

- TODO
- TODO
- TODO

### İlk Hipotezler

1. TODO
2. TODO
3. TODO

### Kontrol Edilecek Sinyaller

- TODO
- TODO
- TODO

### İlk Doğrulama Sonuçları

| Hipotez | Kanıt / Gözlem | Durum |
|---|---|---|
| TODO | TODO | Doğrulanmadı |
| TODO | TODO | Doğrulanmadı |

> **Önemli:** Hipotez, kanıtlanmış sonuç değildir.
> Hipotezler veri ile desteklenmeli, zayıflatılmalı veya elenmelidir.
> Korelasyon doğrudan nedensellik olarak yorumlanmamalıdır.

---

## 6. Değerlendirilen Çözüm Yaklaşımları

Senaryo açıldıktan sonra uygulanabilir alternatifler kısa şekilde değerlendirilecektir.

| Yaklaşım | Avantaj | Risk / Dezavantaj | Uygulanabilirlik | Karar |
|---|---|---|---|---|
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |

### Seçilen Yaklaşım

**Karar:**  
TODO

**Neden:**  
TODO

**Dayandığı Kanıt / Gözlem:**  
TODO

> **Önemli:** Yalnızca hangi yaklaşımın seçildiği değil,
> neden seçildiği ve kararın hangi bilgiye dayandığı da kaydedilmelidir.

---

## 7. AI Stratejisi

AI'ın gerçek kullanım alanları senaryo ve çözüm ihtiyacına göre belirlenecektir.

### Olası AI Kullanım Alanları

- Problem analizi ve alternatif yaklaşım üretimi
- Veri keşfi
- Hipotez üretimi ve değerlendirilmesi
- Kod geliştirme desteği
- Hata ayıklama
- Test senaryosu üretimi
- Sonuçların açıklanması
- Gerektiğinde model karşılaştırması

> Final durumda yalnızca gerçekten gerçekleştirilen AI kullanım alanları bırakılmalıdır.

### İnsan Kontrolünde Kalacak Kritik Kararlar

Örnek:

- Problem tanımının doğrulanması
- Nihai çözüm yaklaşımının seçilmesi
- Kapsam kararlarının verilmesi
- Mimari kararların onaylanması
- AI tarafından üretilen kodun incelenmesi ve çalıştırılması
- Metriklerin doğruluğunun kontrol edilmesi
- Sonuç ve açıklamaların kanıtlarla doğrulanması
- Final teslim kararının verilmesi

### Planlanan İş Akışı

```text
[ Senaryo + Veri ]
        |
        v
[ Problem Çerçeveleme ]
        |
        v
[ Veri Keşfi + Hipotezler ]
        |
        v
[ İnsan Kararı ]
        |
        v
[ AI Destekli Geliştirme ]
        |
        v
[ Test + Doğrulama ]
        |
        v
[ Sonuç + Neden + Kanıt ]
```

Kritik kullanılan prompt'lar:

[`../prompts/`](../prompts/)

> **Önemli:** AI çıktısı nihai gerçek olarak kabul edilmemelidir.
> Kritik sonuçlar veri, kod veya test çıktılarıyla doğrulanmalıdır.

---

## 8. Veri Keşfi Planı

Senaryo verisi alındığında aşağıdaki kontroller ihtiyaç doğrultusunda gerçekleştirilecektir:

- [ ] Veri formatı ve dosya yapısı belirlendi
- [ ] Kolon / alan isimleri incelendi
- [ ] Veri tipleri kontrol edildi
- [ ] Eksik / boş değerler incelendi
- [ ] Zaman alanları varsa doğrulandı
- [ ] Senaryoyla ilgili durum / hata / olay alanları belirlendi
- [ ] Önemli olabilecek sinyaller çıkarıldı
- [ ] Gerekli temel metrikler hesaplandı
- [ ] Dağılım, yoğunlaşma veya değişimler incelendi
- [ ] İlk hipotezler veriyle karşılaştırıldı
- [ ] Veri kalitesinin çözüm üzerindeki olası etkileri değerlendirildi

> **Not:** Amaç doğrudan kod üretmek değil, önce hangi verinin ve sinyalin problem açısından anlamlı olduğunu belirlemektir.

---

## 9. Teknik Yaklaşım

TODO — Senaryo sonrasında gerçekten seçilen teknik yaklaşım özetlenecektir.

### Veri Girdisi

TODO

### Veri İşleme

TODO

### Analiz / Karar Mantığı

TODO

### AI / LLM Kullanımı

TODO

### Açıklanabilirlik

TODO

### Kullanıcı Çıktısı / Arayüz

TODO

### Doğrulama

TODO — Çözümün doğru çalıştığının nasıl kontrol edildiğini açıklayın.

Detaylı teknik mimari:

[`mimari.md`](mimari.md)

> **Önemli:** Final durumda yalnızca gerçekten geliştirilmiş bileşenler ve akışlar anlatılmalıdır.

---

## 10. Riskler

Senaryo ve seçilen çözüm doğrultusunda gerçek riskler bu bölümde takip edilecektir.

| Risk | Etki | Olasılık | Önlem / Aksiyon | Durum |
|---|---|---|---|---|
| AI çıktısının hatalı veya kanıtsız olması | TODO | TODO | Veri / test çıktılarıyla doğrulamak | Açık |
| Geliştirme süresinin yetmemesi | TODO | TODO | MVP kapsamını erken netleştirmek | Açık |
| AI aracı / model erişim problemi | TODO | TODO | Kullanılabilir alternatif yaklaşımı belirlemek | Açık |
| Veri yapısının beklenenden farklı olması | TODO | TODO | İlk aşamada veri yapısını ve kaliteyi doğrulamak | Açık |
| Kurulumun farklı ortamda çalışmaması | TODO | TODO | Çalıştırma adımlarını yeniden test etmek | Açık |
| Git çakışması veya ekip değişikliklerinin üzerine yazılması | TODO | TODO | Düzenli pull, küçük commit ve görev ayrımı | Açık |
| TODO | TODO | TODO | TODO | TODO |

> **Not:** Bunlar başlangıç riskleridir.
> Final durumda yalnızca gerçek çözüm açısından anlamlı olan riskler bırakılmalı,
> ortaya çıkan yeni kritik riskler eklenmelidir.

---

## 11. Zaman Planı

Resmi etkinlik akışı:

- **14:30** — Senaryo ve veri paketinin paylaşılması
- **14:30 – 14:45** — Toplu soru penceresi
- **14:45 – 17:30** — Geliştirme
- **17:30** — Final teslim

Aşağıdaki zamanlar ekip içi hedef plandır ve senaryonun ihtiyaçlarına göre gerektiğinde ayarlanabilir.

### 14:30 – 14:45 | Senaryo Analizi ve İlk Plan

- Senaryoyu birlikte okumak
- Veri paketini hızlıca incelemek
- Problem tanımını oluşturmak
- Açık soruları belirlemek
- Gerekli soruları toplu soru penceresinde sormak
- İlk başarı kriterlerini belirlemek
- Alternatif çözüm yaklaşımlarını değerlendirmek
- Ekip içi görev dağılımını netleştirmek

> İlk aşamada doğrudan kapsamlı kod geliştirmeye başlamak yerine problem ve yaklaşımın netleştirilmesine öncelik verilecektir.

### 14:45 – 15:15 | Veri Keşfi ve Yaklaşımın Doğrulanması

- Veri yapısını incelemek
- Veri kalitesini kontrol etmek
- Önemli sinyalleri belirlemek
- İlk hipotezleri test etmek
- Seçilecek yaklaşımı veriye göre doğrulamak
- MVP kapsamını netleştirmek

### 15:15 – 16:15 | Çekirdek Çözümün Geliştirilmesi

- Temel veri işleme akışını oluşturmak
- Ana analiz / çözüm mantığını geliştirmek
- Modülleri ayrı ayrı çalıştırmak ve doğrulamak
- İlk uçtan uca çalışan akışı oluşturmak
- Anlamlı ara commit'ler oluşturmak

### 16:15 – 16:45 | AI Entegrasyonu, XAI ve X-Factor

- Gerçek ihtiyaç olan AI entegrasyonlarını tamamlamak
- Sonuçların açıklanabilirliğini geliştirmek
- X-Factor özelliğini tamamlamak
- Kanıt yollarını belirlemek
- Gerekiyorsa model karşılaştırması yapmak

### 16:45 – 17:05 | Test, Stabilizasyon ve Ölçüm

- Uçtan uca test yapmak
- Kritik hataları düzeltmek
- Edge case'leri kontrol etmek
- Gerçek metrikleri ölçmek
- Sonuç ve açıklamaları doğrulamak
- Demo akışını test etmek

### 17:05 – 17:20 | Dokümantasyon ve Demo Hazırlığı

- `README.md` güncellemek
- `AI_JURI.md` tamamlamak
- `submission.json` güncellemek
- `docs/mimari.md` güncellemek
- `docs/fazlar.md` güncellemek
- Kritik kullanılan prompt'ları kaydetmek
- Ekran görüntülerini ve demo kanıtlarını eklemek
- Bilinen sınırları güncellemek

### 17:20 – 17:30 | Final Kontrol ve Teslim

- Çalıştırma komutunu son kez test etmek
- README / AI_JURI / submission tutarlılığını kontrol etmek
- Model adları ve sürümlerini doğrulamak
- X-Factor kanıt yollarını doğrulamak
- TODO / placeholder kontrolü yapmak
- `.env` ve hassas veri kontrolü yapmak
- `git status` kontrol etmek
- Final commit oluşturmak
- Final push yapmak
- GitHub üzerindeki son commit'i doğrulamak

> **KRİTİK:** Değerlendirme 17:30'daki son commit üzerinden yapılacaktır.
> Final push mümkün olduğunca son dakikaya bırakılmamalıdır.

---

## 12. Çıktılar / Deliverables

Hackathon sonunda aşağıdaki çıktıların hazır olması hedeflenmektedir:

- [ ] Çalışan kaynak kod
- [ ] Tanımlanmış komutla çalıştırılabilen çözüm
- [ ] Güncel `README.md`
- [ ] Güncel `AI_JURI.md`
- [ ] Güncel ve geçerli `submission.json`
- [ ] Güncel `docs/mimari.md`
- [ ] Güncel `docs/fazlar.md`
- [ ] Gerçekten kullanılan kritik prompt kayıtları
- [ ] Gerçekten ölçülen metrikler
- [ ] Gerekli ekran görüntüleri / demo kanıtları
- [ ] Test edilmiş demo akışı
- [ ] Güncel bilinen sınırlar

---

## 13. Plan Değişiklikleri

Hackathon sırasında ana yaklaşım, kapsam veya önemli bir teknik karar değişirse burada kısa şekilde kaydedilecektir.

| Zaman | Değişiklik | Neden / Kanıt |
|---|---|---|
| TODO | TODO | TODO |

> **Not:** Buradaki amaç her küçük değişikliği kaydetmek değil;
> çözümün yönünü etkileyen önemli kararları ve nedenlerini görünür kılmaktır.

---

## 14. İlgili Dokümanlar

- [`fazlar.md`](fazlar.md) — Faz bazlı ilerleme ve kontrol
- [`mimari.md`](mimari.md) — Teknik mimari
- [`../AI_JURI.md`](../AI_JURI.md) — AI Jüri özeti
- [`../README.md`](../README.md) — Projenin ana dokümanı
- [`../submission.json`](../submission.json) — Makine tarafından okunabilir proje künyesi
- [`../prompts/`](../prompts/) — AI prompt şablonları ve gerçek kullanım kayıtları