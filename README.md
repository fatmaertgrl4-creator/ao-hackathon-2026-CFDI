# ao-hackathon-2026-CFDI

CFDI ekibinin **AO Hackathon 2026** projesidir.

> **Durum: TASLAK**
>
> Senaryo henüz açıklanmadığı için probleme ve çözüme özel alanlar `TODO` olarak bırakılmıştır.
> Senaryo ve veri paketi paylaşıldıktan sonra ilgili alanlar yalnızca gerçek çözüm, gerçek ölçümler ve doğrulanmış bilgilerle güncellenecektir.

---

## 1. Proje Özeti

**Proje Adı:**  
TODO

**Tek Cümlelik Özet:**  
TODO

> **Not:** Tek cümlelik özet, `submission.json` → `proje.ozet` alanı ile tutarlı olmalıdır.

---

## 2. Çözdüğümüz Problem

TODO — Senaryo açıklandıktan sonra aşağıdaki bilgiler netleştirilecektir:

- Problem nedir?
- Operasyon / SRE açısından etkisi nedir?
- Problem hangi veri veya sinyaller üzerinden gözlemlenmektedir?
- Çözümden beklenen temel çıktı nedir?
- Başarı hangi ölçülebilir kriterlerle değerlendirilecektir?

> **Önemli:** Problem tanımı kısa, somut ve senaryoda verilen gerçek bilgilerle uyumlu olmalıdır. Varsayımlar açıkça belirtilmeli, doğrulanmamış bilgiler gerçekmiş gibi sunulmamalıdır.

---

## 3. Çözümümüz Nasıl Çalışıyor?

TODO — Gerçek çözüm geliştirildikten sonra uçtan uca çalışma akışı açıklanacaktır.

Aşağıdaki yapı ihtiyaç halinde kullanılabilir:

1. Veri paketi alınır.
2. Veri yapısı ve ilgili sinyaller incelenir.
3. Olası anomali ve problem göstergeleri analiz edilir.
4. İlgili metrikler ve kanıtlar çıkarılır.
5. Çözümün ihtiyaç duyduğu noktalarda AI destekli analiz gerçekleştirilir.
6. Sonuçlar gerekçeleri ve kanıtlarıyla birlikte kullanıcıya sunulur.

Detaylı mimari:

[`docs/mimari.md`](docs/mimari.md)

> **Önemli:** Final dokümantasyonda yalnızca gerçekten geliştirilmiş akış anlatılmalıdır. “AI analiz ediyor” gibi genel ifadeler yerine verinin sisteme nasıl girdiği, nasıl işlendiği ve hangi çıktının üretildiği somut şekilde açıklanmalıdır.

---

## 4. Kurulum

### Ön Koşullar

TODO — Gerçekte kullanılan teknoloji ve bağımlılıklara göre güncellenecektir.

Örnek:

- Python 3.11+
- ve/veya Node.js 20+
- Git
- Projenin ihtiyaç duyduğu bağımlılıklar
- Gerekli ortam değişkenleri

### Repoyu Klonlayın

```bash
git clone https://github.com/fatmaertgrl4-creator/ao-hackathon-2026-CFDI.git
cd ao-hackathon-2026-CFDI
```

### Ortam Değişkenlerini Hazırlayın

Linux / macOS:

```bash
cp .env.example .env
```

PowerShell:

```powershell
Copy-Item .env.example .env
```

Ardından yalnızca uygulamanın gerçekten ihtiyaç duyduğu değerleri `.env` dosyasına ekleyin.

> **Önemli:** Gerçek `.env` dosyası kesinlikle repoya commit edilmemelidir. API key, token, parola veya diğer gizli bilgiler public repoda bulunmamalıdır.

### Bağımlılıkları Kurun

```bash
TODO
```

### Uygulamayı Çalıştırın

```bash
TODO
```

**Beklenen çıktı:**  
TODO

> **Önemli:** Final çalıştırma komutu `README.md`, `AI_JURI.md` ve `submission.json` → `calistirma.komut` alanlarında aynı ve güncel olmalıdır.

---

## 5. AI Stratejimiz ve İş Akışı

Hackathon sırasında AI, çözümün gerçekten ihtiyaç duyduğu aşamalarda kullanılacaktır.

Olası kullanım alanları:

- Problem analizi ve planlama
- Veri keşfi
- Hipotez üretimi ve değerlendirilmesi
- Kod geliştirme desteği
- Hata ayıklama
- Test senaryosu üretimi
- Sonuçların açıklanması
- Gerektiğinde model karşılaştırması

Kullanılan kritik prompt'lar:

[`prompts/`](prompts/)

> **Önemli:** Final durumda bu bölüm yalnızca yarışma sırasında gerçekten kullanılan AI aşamalarını içermelidir. Kritik kullanılan prompt'lar `prompts/` altında saklanarak AI iş akışının kanıtı olarak gösterilecektir.

---

## 6. Kullanılan AI Araçları ve Model Sürümleri

| Platform / Araç | Model | Sürüm | Kullanım Amacı |
|---|---|---|---|
| SAKA | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

> **Önemli:** Yalnızca gerçekten kullanılan AI araçları, model adları ve doğrulanmış model sürümleri yazılmalıdır. SAKA dışında kullanılan araçlar varsa eklenmeli; kullanılmayan veya sürümü doğrulanamayan bir araç varmış gibi gösterilmemelidir.

---

## 7. İnsan – AI İş Bölümü

TODO — Yarışma sırasında AI'ın hangi görevlerde kullanıldığı ve hangi kritik kararların ekip tarafından verildiği açıklanacaktır.

Örnek yapı:

| Aşama | AI'ın Rolü | İnsan Kararı / Doğrulaması |
|---|---|---|
| Problem analizi | Hipotez ve alternatif üretmek | Problemi ve yaklaşımı doğrulamak |
| Veri keşfi | İncelenebilecek sinyalleri önermek | Sinyalleri gerçek veride doğrulamak |
| Kodlama | Kod taslağı veya öneri üretmek | Kodu incelemek ve çalıştırmak |
| Test | Test senaryoları önermek | Sonuçları doğrulamak |
| Sonuç | Açıklama taslağı üretmek | Nihai yorumu ve kanıtı onaylamak |

> **Önemli:** Final tabloda yalnızca gerçekten gerçekleştirilen görevler yer almalıdır.

---

## 8. Açıklanabilirlik — XAI

TODO — Çözüm bir karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa bunun nedenini ve dayandığı kanıtları nasıl gösterdiği açıklanacaktır.

Temel yaklaşım:

**SONUÇ + NEDEN + KANIT**

Gerekli olduğunda aşağıdaki yapı kullanılabilir:

- **RESULT:** Üretilen sonuç
- **REASON:** Sonucun gerekçesi
- **EVIDENCE:** Dayanılan veri / kanıt
- **CONFIDENCE / UNCERTAINTY:** Güven veya belirsizlik
- **NEXT CHECK:** Gerekli sonraki kontrol

Örnek yaklaşım:

> “Bir servis kritik” demek yerine, servisin neden kritik değerlendirildiği ve bu değerlendirmenin hangi ölçüm veya gözleme dayandığı birlikte gösterilir.

> **Önemli:** Final örneklerinde yalnızca gerçekten gözlemlenmiş veya ölçülmüş bilgiler kullanılmalıdır. Kanıtlanmayan nedensellik kurulmamalıdır.

---

## 9. X-Factor

TODO — Çözümümüzü standart bir analiz veya veri görüntüleme yaklaşımından ayıran en önemli AI destekli özellik açıklanacaktır.

**X-Factor:**  
TODO

**Neden değerlidir?**  
TODO

**Kod Kanıtı:**

```text
src/<dosya>:<satır_aralığı>
```

> **Önemli:** “AI kullanıyoruz” tek başına X-Factor değildir. X-Factor gerçek üründe çalışmalı, probleme somut değer sağlamalı ve kod veya çıktı ile kanıtlanabilmelidir.

---

## 10. Ölçtüğümüz Metrikler

TODO — Çözümün başarısını veya ürettiği çıktıyı gösteren yalnızca gerçekten ölçülmüş metrikler eklenecektir.

| Metrik | Sonuç | Ölçüm / Hesaplama Yöntemi |
|---|---:|---|
| TODO — Gerçekten ölçülen metrik | TODO | TODO |
| TODO — Gerçekten ölçülen metrik | TODO | TODO |
| TODO — Gerçekten ölçülen metrik | TODO | TODO |

> **Önemli:** Yalnızca gerçekten ölçülen ve nasıl hesaplandığı açıklanabilen metrikler eklenmelidir. Ölçülmeyen bir değer başarı metriği olarak sunulmamalıdır.

---

## 11. MCP Sunucuları

Kullanılan MCP sunucuları:

TODO — Gerçek kullanıma göre güncellenecektir.

MCP kullanılmadıysa final durumda:

> Bu projede MCP sunucusu kullanılmamıştır.

> **Önemli:** Kullanılmayan MCP sunucuları varmış gibi gösterilmemelidir.

---

## 12. Entegre API'ler

Kullanılan API'ler:

TODO — Gerçek kullanıma göre güncellenecektir.

Harici API kullanılmadıysa final durumda:

> Bu projede harici API entegrasyonu kullanılmamıştır.

> **Önemli:** API key, token veya diğer gizli erişim bilgileri README içerisinde paylaşılmamalıdır.

---

## 13. Ekran Görüntüleri ve Demo

Demo materyalleri:

[`demo/`](demo/)

### Ekran Görüntüleri

TODO — Gerçek çalışan çözümden alınan ekran görüntüleri eklenecektir.

### Demo Akışı

1. TODO
2. TODO
3. TODO

### Demo Videosu

TODO — Varsa bağlantı eklenecektir.

> **Önemli:** Demo akışı final ürünün gerçekten yapabildiği işlemlerle uyumlu olmalı ve sunumdan önce test edilmelidir.

---

## 14. Deploy

**Deploy URL:**  
TODO

Deploy yapılmadıysa final durumda:

> Uygulama lokal ortamda çalışmaktadır. Canlı deploy yapılmamıştır.

> **Not:** Canlı deploy zorunlu değildir. Lokal ortamda çalışan ve sahnede gösterilebilen bir çözüm yeterlidir.

---

## 15. Bilinen Sınırlar

TODO — Çözümün gerçek sınırları ve tamamlanamayan noktaları açık şekilde belirtilmelidir.

Örnek yapı:

- TODO
- TODO
- TODO

Mümkünse her önemli sınır için aşağıdakiler kısaca belirtilir:

- Mevcut durum
- Sınırın nedeni
- Daha fazla süre olması halinde nasıl geliştirilebileceği

> **Önemli:** Bilinen eksikler veya sınırlar saklanmamalı; çözüm olduğundan daha kapsamlı gösterilmemelidir.

---

## 16. Repo Yapısı

```text
ao-hackathon-2026-CFDI/
│
├── README.md
├── AI_JURI.md
├── submission.json
├── .env.example
├── .gitignore
├── CLAUDE.md
│
├── docs/
│   ├── plan.md
│   ├── fazlar.md
│   └── mimari.md
│
├── prompts/
│   ├── README.md
│   ├── _SABLON.md
│   ├── templates/
│   └── used/
│
├── demo/
└── src/
```

| Yol | Açıklama |
|---|---|
| `README.md` | Projenin ana açıklaması ve çalıştırma talimatları |
| `AI_JURI.md` | AI Jüri için yapılandırılmış çözüm özeti |
| `submission.json` | Makine tarafından okunabilir proje künyesi |
| `.env.example` | Ortam değişkeni şablonu |
| `CLAUDE.md` | AI geliştirme aracı için repo çalışma talimatları |
| `docs/` | Plan, fazlar ve mimari dokümanları |
| `prompts/` | AI kullanımına ilişkin prompt ve kanıtlar |
| `prompts/templates/` | Yarışma öncesi hazırlanmış genel amaçlı prompt şablonları |
| `prompts/used/` | Yarışma sırasında gerçekten kullanılan kritik prompt kayıtları |
| `demo/` | Ekran görüntüleri ve demo materyalleri |
| `src/` | Kaynak kod |

> **Not:** `templates/` ve `used/` klasörleri ekip içi düzen amacıyla kullanılmaktadır. Final repo yapısı gerçek kullanılan dosyalarla uyumlu tutulmalıdır.

---

## 17. Ekip

| Ekip Üyesi | Rol / Sorumluluk |
|---|---|
| TODO | TODO |
| TODO | TODO |
| TODO | TODO |

> **Not:** Ekip bilgileri `submission.json` → `takim.uyeler` alanı ile tutarlı olmalıdır.

---

## Final Teslim Kontrolü

Teslimden önce aşağıdakiler kontrol edilmelidir:

- [ ] Proje adı ve tek cümlelik özet ilgili dokümanlarda tutarlı
- [ ] README gerçek çalışan çözümü anlatıyor
- [ ] `AI_JURI.md` güncel
- [ ] `submission.json` güncel
- [ ] `submission.json` geçerli JSON formatında
- [ ] Çalıştırma komutu README, `AI_JURI.md` ve `submission.json` içerisinde aynı
- [ ] Kullanılan tüm AI araçları ve doğrulanmış model sürümleri yazılmış
- [ ] Kritik kullanılan prompt'lar `prompts/` altında kayıtlı
- [ ] X-Factor gerçek ve kod veya çıktı ile kanıtlanmış
- [ ] X-Factor dosya ve satır referansları final kodla doğrulanmış
- [ ] Yazılan metriklerin tamamı gerçekten ölçülmüş
- [ ] MCP ve API bilgileri gerçek kullanım ile uyumlu
- [ ] Ekran görüntüleri gerçek çalışan çözümden alınmış
- [ ] Demo akışı final ürünle uyumlu
- [ ] Kurulum ve çalıştırma adımları test edilmiş
- [ ] Bilinen sınırlar güncel
- [ ] Gerçek `.env` dosyası repoya commit edilmemiş
- [ ] API key, token, parola veya hassas veri repoda bulunmuyor
- [ ] Gereksiz test, debug ve geçici dosyalar kontrol edilmiş
- [ ] Repo public durumda
- [ ] Final commit ve push en geç 17:30 teslim saatine kadar tamamlanmış
- [ ] Final push sonrasında `git status` ile yerel ve remote durumun senkron olduğu doğrulanmış