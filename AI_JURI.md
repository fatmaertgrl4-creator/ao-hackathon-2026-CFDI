# AI Jüri Özeti

> **DURUM: TASLAK — final teslim için henüz hazır değildir.**
>
> Senaryo henüz açıklanmadığı için çözüme özel alanlar `TODO` olarak bırakılmıştır.
> Senaryo ve veri paketi paylaşıldıktan sonra bu alanlar yalnızca gerçek çözüm,
> doğrulanmış sonuçlar ve repository içerisinde gösterilebilen kanıtlarla güncellenecektir.
>
> Bu dokümandaki önemli iddialar gerçek dosya, kod, çıktı veya ölçüm kanıtıyla desteklenmelidir.
> Var olmayan dosya, özellik, metrik veya satır aralığı referans olarak verilmemelidir.

**Takım:** CFDI  
**Repo:** https://github.com/fatmaertgrl4-creator/ao-hackathon-2026-CFDI

---

## 1. AI Stratejimiz ve İş Akışı

### Kullandığımız AI Araçları

| Araç / Platform | Model | Sürüm | Kullanım Amacı |
|---|---|---|---|
| SAKA | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

> Final durumda yalnızca gerçekten kullanılan araçlar, gerçek model adları ve doğrulanmış sürümler yer almalıdır.

### AI'ı Nasıl Kullandık?

TODO — AI'ın gerçekten kullanıldığı aşamaları ve her aşamada ne amaçla kullanıldığını somut şekilde açıklayın.

Olası kullanım alanları:

- Problem analizi ve planlama
- Veri keşfi
- Hipotez üretimi ve değerlendirilmesi
- Kod geliştirme desteği
- Hata ayıklama
- Test senaryosu üretimi
- Sonuçların açıklanması
- Gerektiğinde model karşılaştırması

> Final durumda yalnızca gerçekten gerçekleştirilen AI kullanım adımları bırakılmalıdır.

### İnsan – AI İş Bölümü

TODO — AI'ın yaptığı işleri ve kritik insan kararlarını açıklayın.

Örnek yapı:

| Aşama | AI'ın Rolü | İnsan Kararı / Doğrulaması |
|---|---|---|
| Problem analizi | Hipotez ve alternatif üretmek | Problemi ve yaklaşımı doğrulamak |
| Veri keşfi | İncelenebilecek sinyalleri önermek | Sinyalleri gerçek veride doğrulamak |
| Kodlama | Kod taslağı veya öneri üretmek | Kodu incelemek ve çalıştırmak |
| Test | Test senaryoları önermek | Sonuçları doğrulamak |
| Sonuç | Açıklama taslağı üretmek | Nihai yorumu ve kanıtı onaylamak |

### İş Akışımız

TODO — Gerçekte uygulanan AI destekli çalışma akışını kısa ve açık şekilde anlatın.

Örnek yapı:

**Problem tanımlama → veri keşfi → hipotezler → yaklaşım seçimi → geliştirme → test → açıklama → doğrulama**

> **Önemli:** “AI ile kod yazdık” tek başına yeterli bir açıklama değildir.
> AI'ın hangi görevde ne ürettiği, ekibin bu çıktıyı nasıl değerlendirdiği
> ve son kararın nasıl doğrulandığı açıklanmalıdır.

### Kanıt

- [`prompts/`](prompts/)
- [`CLAUDE.md`](CLAUDE.md)
- [`docs/plan.md`](docs/plan.md)
- TODO — yarışma sırasında oluşan diğer gerçek kanıt yolları

---

## 2. Problemi Nasıl Çözdük

### Problem ve Yaklaşım

TODO — Problemi nasıl anladığımızı, nasıl parçaladığımızı ve neden seçilen yaklaşımı kullandığımızı açıklayın.

Aşağıdaki sorular cevaplanmalıdır:

- Problem neydi?
- Operasyon / SRE açısından etkisi neydi?
- Hangi veri ve sinyalleri inceledik?
- Hangi hipotezleri değerlendirdik?
- Hangi yaklaşımı seçtik?
- Bu yaklaşımı neden seçtik?
- Hangi varsayımlar doğrulandı, hangileri elendi?

Doğrulanmamış hipotezler gerçek nedenmiş gibi sunulmamalıdır.

### Çalışan Çözüm

TODO — Gerçekte geliştirilen çözümün uçtan uca nasıl çalıştığını anlatın.

Açıklanabilecek noktalar:

- Sistem hangi girdileri alıyor?
- Veriyi nasıl işliyor?
- Hangi analizleri gerçekleştiriyor?
- AI hangi noktada ve hangi amaçla kullanılıyor?
- Kullanıcıya hangi çıktıları veriyor?
- Sonuçların gerekçesi veya kanıtı nasıl gösteriliyor?

Final açıklama gerçek `src/` içeriğiyle uyumlu olmalıdır.

### Ölçtüğümüz Sonuçlar

TODO — Yalnızca gerçekten ölçülmüş sonuçları ekleyin.

| Metrik | Sonuç | Ölçüm / Hesaplama Yöntemi |
|---|---:|---|
| TODO — Gerçekten ölçülen metrik | TODO | TODO |
| TODO — Gerçekten ölçülen metrik | TODO | TODO |
| TODO — Gerçekten ölçülen metrik | TODO | TODO |

> **Önemli:**
>
> “Hızlı”, “başarılı”, “yüksek doğruluk” gibi ifadeler yalnızca ölçümle desteklenebiliyorsa kullanılmalıdır.
>
> Ölçülmeyen veya hesaplanamayan bir değer metrik olarak sunulmamalıdır.

### Kanıt

- [`src/`](src/)
- [`docs/mimari.md`](docs/mimari.md)
- [`demo/`](demo/)
- TODO — ölçüm veya çıktıların bulunduğu gerçek dosya / dosyalar

---

## 3. X-Factor

### X-Factor'ımız

TODO — Çözümümüzü standart bir analiz, dashboard veya veri görüntüleme yaklaşımından ayıran en güçlü AI destekli özelliği açıklayın.

Final durumda burada mümkün olduğunca **tek ve net bir X-Factor** anlatılmalıdır.

> **Önemli:**
>
> “AI kullanıyoruz” tek başına X-Factor değildir.
> Özellik gerçek çözümde çalışmalı ve somut kanıtla gösterilebilmelidir.

### Neden Değer Katıyor?

TODO — Bu özelliğin probleme hangi ek değeri sağladığını açıklayın.

Aşağıdaki sorular yardımcı olabilir:

- Kullanıcıya hangi yeni kabiliyeti sağlıyor?
- Operasyonel karar vermeyi nasıl kolaylaştırıyor?
- AI burada neden anlamlı bir rol oynuyor?
- Üretilen sonuç nasıl açıklanabiliyor veya doğrulanabiliyor?
- Demo sırasında bu değer nasıl gösterilecek?

AI kullanılmasının tek başına değer olduğu varsayılmamalıdır.

### Kod Kanıtı

```text
src/<gerçek_dosya_adı>:<gerçek_satır_aralığı>
```

### Çıktı / Demo Kanıtı

```text
TODO — demo/<gerçek_dosya_veya_ekran_görüntüsü>
```

> **Önemli:** Dosya adı ve satır aralığı final commit üzerinden doğrulanmalıdır.
> Tahmini, eski veya var olmayan referans kullanılmamalıdır.

---

## 4. Çalıştırma

### Ön Koşullar

TODO — Gerçekte kullanılan teknoloji ve bağımlılıklara göre güncelleyin.

Örnek:

- Python 3.11+
- ve/veya Node.js 20+
- Gerekli bağımlılıklar
- Gerekli ortam değişkenleri

### Kurulum

```bash
TODO
```

### Tek Komut

```bash
TODO
```

### Beklenen Çıktı

TODO — Komut çalıştırıldığında kullanıcının veya jürinin ne göreceğini açık şekilde yazın.

Örneğin:

- Web arayüzünün açılacağı adres
- Terminalde görülecek başlangıç mesajı
- Oluşacak çıktı veya rapor
- Demo için izlenecek ilk adım

> **Önemli:** Final çalıştırma komutu:
>
> - `README.md`
> - `AI_JURI.md`
> - `submission.json` → `calistirma.komut`
>
> içerisinde aynı olmalıdır.
>
> Final teslimden önce kurulum ve çalıştırma adımları gerçekten test edilmelidir.

### Kanıt

- [`README.md`](README.md)
- [`.env.example`](.env.example)
- TODO — gerçek dependency / requirements dosyası
- TODO — gerekiyorsa gerçek entry-point dosyası

---

## 5. Bilinen Sınırlar

TODO — Çözümün yapamadığı, sınırlı kaldığı veya henüz doğrulanamayan noktaları açık şekilde belirtin.

Önerilen format:

### Sınır 1

**Sınırlı Kalan Nokta:** TODO  
**Neden:** TODO  
**Etkisi:** TODO  
**Nasıl Geliştirilebilir:** TODO

### Sınır 2

**Sınırlı Kalan Nokta:** TODO  
**Neden:** TODO  
**Etkisi:** TODO  
**Nasıl Geliştirilebilir:** TODO

> **Önemli:**
>
> Bilinen sınırlar gizlenmemeli ve çözüm gerçekte olduğundan daha kapsamlı gösterilmemelidir.
> Yalnızca gerçekten bilinen veya gözlemlenen sınırlamalar yazılmalıdır.
>
> Yarışma öncesi geçici notlar ve artık geçerli olmayan `TODO` alanları final teslimden önce temizlenmelidir.

### Kanıt

TODO — Her önemli sınır için mümkün olduğunda ilgili gerçek dosya, kod bölümü, test sonucu veya çıktı belirtilmelidir.

Örnek format:

```text
src/<dosya>:<satır_aralığı>
demo/<çıktı>
docs/<ilgili_doküman>
```

---

## Final Kontrol

Final teslimden önce:

- [ ] Beş ana bölüm gerçek çözümle güncel
- [ ] Tüm `TODO` alanları kontrol edilmiş
- [ ] Kullanılan AI araçları ve model sürümleri doğrulanmış
- [ ] İnsan – AI iş bölümü gerçek süreçle uyumlu
- [ ] Kritik prompt kanıtları mevcut
- [ ] Problem ve çözüm anlatımı gerçek kodla uyumlu
- [ ] Metrikler gerçekten ölçülmüş
- [ ] X-Factor tek, net ve kanıtlanabilir
- [ ] X-Factor dosya / satır referansı final kod üzerinden doğrulanmış
- [ ] Çalıştırma komutu README ve `submission.json` ile aynı
- [ ] Çalıştırma adımları test edilmiş
- [ ] Bilinen sınırlar güncel ve dürüst
- [ ] Var olmayan dosya, özellik, metrik veya kanıt referansı bulunmuyor