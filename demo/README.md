# Demo

Bu dizin, çözümün **çalışan ürün çıktısını, görsel kanıtlarını ve canlı demo akışını** belgelemek için kullanılır.

`demo/`, özellikle `AI_JURI.md` içerisindeki:

- **2. Problemi Nasıl Çözdük**
- **3. X-Factor**

bölümlerindeki iddiaları destekleyen kanıt kaynaklarından biri olabilir.

> **Durum: TASLAK**
>
> Senaryo ve çözüm henüz kesinleşmediği için demo adımları `TODO` durumundadır.
> Gerçek ürün ortaya çıktıkça bu dosya yalnızca gerçek demo akışı,
> gerçek ekran görüntüleri ve doğrulanmış çıktılarla güncellenecektir.

---

## 1. Demo Amacı

TODO — Canlı demoda jüriye hangi problemi, çözümün hangi temel yeteneğini
ve hangi somut sonucu göstereceğimizi kısa şekilde açıklayın.

Demo mümkün olduğunca aşağıdaki mantığı görünür kılmalıdır:

```text
Problem / Girdi
      ↓
Çözüm Çalışıyor
      ↓
Gerçek Sonuç
      ↓
Gerekçe / Kanıt
      ↓
X-Factor
```

AI çalışan ürünün bir parçasıysa ilgili noktada ayrıca gösterilebilir:

```text
Problem / Girdi
      ↓
Temel Analiz / İşleme
      ↓
AI'ın Gerçek Görevi
      ↓
Doğrulama
      ↓
Sonuç + Kanıt
```

> **Önemli:** Demo yalnızca güzel bir arayüz göstermek için değil,
> çözümün senaryodaki problemi gerçekten nasıl ele aldığını kanıtlamak için kullanılmalıdır.
>
> AI ürün içerisinde kullanılmıyorsa sırf AI göstermek amacıyla yapay bir demo adımı eklenmemelidir.

---

## 2. Demo Akışı

Final canlı demo adımları burada tutulacaktır.

Bu akış:

```text
submission.json → sunum.demo_akisi
```

ile anlam ve sıra bakımından tutarlı olmalıdır.

### Adım 1 — TODO

**Amaç:**  
TODO

**Gösterilecek:**  
TODO

**Anlatılacak:**  
TODO

**Kanıtlanan özellik / sonuç:**  
TODO

**İlgili ekran görüntüsü:**  
`01-TODO.png`

---

### Adım 2 — TODO

**Amaç:**  
TODO

**Gösterilecek:**  
TODO

**Anlatılacak:**  
TODO

**Kanıtlanan özellik / sonuç:**  
TODO

**İlgili ekran görüntüsü:**  
`02-TODO.png`

---

### Adım 3 — TODO

**Amaç:**  
TODO

**Gösterilecek:**  
TODO

**Anlatılacak:**  
TODO

**Kanıtlanan özellik / sonuç:**  
TODO

**İlgili ekran görüntüsü:**  
`03-TODO.png`

---

> **Not:** Demo adım sayısı gerçek çözümün ihtiyaçlarına göre artırılabilir veya azaltılabilir.
>
> Gereksiz ekranlar eklenmemeli; jüri birkaç dakika içerisinde:
>
> **problem → çalışan çözüm → gerçek sonuç → kanıt → X-Factor**
>
> ilişkisini anlayabilmelidir.

---

## 3. Ekran Görüntüleri

Gerçek ekran görüntüleri bu dizinde anlaşılır dosya adlarıyla saklanmalıdır.

Önerilen isimlendirme:

```text
01-<kisa-aciklama>.png
02-<kisa-aciklama>.png
03-<kisa-aciklama>.png
```

Örnek biçim:

```text
01-girdi.png
02-analiz-sonucu.png
03-aciklanabilirlik.png
04-x-factor.png
```

> Bunlar yalnızca isimlendirme örnekleridir.
> Final dosya adları gerçek çözümü yansıtmalıdır.

Her ekran görüntüsü:

- Gerçek çalışan çözümden alınmalı
- Final davranışla uyumlu olmalı
- Kritik çıktıyı mümkün olduğunca görünür göstermeli
- Gizli veya hassas bilgi içermemeli

> Boş arayüz, mock ekran veya yalnızca dekoratif görüntü yerine,
> ürünün gerçekten ne yaptığını gösteren kanıt niteliğindeki ekranlar tercih edilmelidir.

---

## 4. Demo İçerisinde Gösterilebilecek Kanıtlar

Gerçek senaryo ve çözüm uygun olduğu ölçüde aşağıdakiler gösterilebilir:

- Sisteme verilen girdi
- Temel analiz / işleme sonucu
- Senaryoda beklenen temel çıktı
- Gerçek ölçülen değer veya metrik
- Karar / öneri / tespit varsa gerekçesi
- Sonucu destekleyen veri veya kanıt
- AI gerçekten kullanılıyorsa AI'ın somut katkısı
- AI çıktısının nasıl doğrulandığı
- X-Factor
- X-Factor'ın çalışan sonucu

> Finalde yalnızca gerçekten geliştirilen ve doğrulanan özellikler gösterilmelidir.
>
> Demo akışına sırf etkileyici görünmesi için gerçek üründe bulunmayan özellik eklenmemelidir.

---

## 5. Açıklanabilirlik / XAI Demo Kanıtı

Çözüm bir karar, tespit, sınıflandırma, önceliklendirme veya öneri üretiyorsa
demo sırasında yalnızca sonucu değil, mümkün olduğunda **nedenini ve kanıtını**
da göstermek hedeflenmelidir.

Temel yapı:

```text
SONUÇ
   +
NEDEN
   +
KANIT
```

Gerekirse:

```text
RESULT
REASON
EVIDENCE
CONFIDENCE / UNCERTAINTY
NEXT CHECK
```

Örnek biçim:

```text
SONUÇ:
TODO — Gerçek sistem sonucu

NEDEN:
TODO — Sonucun gerçek gerekçesi

KANIT:
TODO — Sonucu destekleyen gerçek veri / ölçüm / çıktı
```

> **Önemli:** Final demo örnekleri yalnızca gerçek hackathon verisine
> ve gerçek çalışan çözümün çıktısına dayanmalıdır.
>
> Model tarafından üretilmiş fakat veri veya sistem çıktısıyla desteklenmeyen
> açıklamalar kanıt olarak gösterilmemelidir.
>
> Kesin olmayan bir sonuç varsa bu durum açıkça belirtilmelidir.

---

## 6. X-Factor Demo Anı

**X-Factor:**

TODO

**Demoda hangi adımda gösterilecek:**

TODO

**Kullanıcıya / operasyona sağladığı değer:**

TODO

**Jüriye verilecek ana mesaj:**

TODO

**Ana kod kanıtı:**

```text
src/<gercek_dosya>:<gercek_satir_araligi>
```

Gerekirse ek kod kanıtları:

```text
TODO
```

**Çalışan ürün / çıktı kanıtı:**

```text
TODO
```

> X-Factor mümkün olduğunca tek ve anlaşılır bir demo anında görünür hale getirilmelidir.
>
> Yalnızca kodda bulunması yeterli değildir;
> mümkün olduğunda gerçekten çalışan sonucu da gösterilmelidir.
>
> Dosya ve satır referansları final kod değişikliklerinden sonra yeniden doğrulanmalıdır.

---

## 7. Ölçülen Sonuçlar

Demo sırasında gösterilecek gerçek ölçümler burada tutulacaktır.

| Metrik | Gerçek Sonuç | Ölçüm / Hesaplama Yöntemi | Demo Adımı |
|---|---:|---|---|
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

> **Önemli:** Yalnızca gerçekten ölçülmüş sonuçlar kullanılmalıdır.
>
> Ölçülmemiş:
>
> - başarı oranı
> - doğruluk
> - hız artışı
> - zaman tasarrufu
> - performans iyileşmesi
>
> gibi değerler tahmin edilerek yazılmamalıdır.

Gösterilen metrikler ilgili final dokümantasyonla tutarlı olmalıdır.

---

## 8. AI Kullanımının Demo Edilmesi

AI çalışan ürünün gerçek bir parçasıysa demo sırasında aşağıdaki sorular mümkün olduğunca cevaplanabilmelidir:

- AI ne yapıyor?
- Neden burada AI kullanılıyor?
- AI'a hangi bağlam veriliyor?
- AI ne üretiyor?
- Çıktı doğrudan mı kullanılıyor?
- Nasıl doğrulanıyor?
- AI başarısız olursa sistem nasıl davranıyor?

**Gerçek AI demo noktası:**

TODO

**Doğrulama:**

TODO

> AI yalnızca geliştirme sürecinde kodlama veya analiz desteği için kullanıldıysa,
> bu durum AI stratejisi bölümünde anlatılabilir.
> Çalışan üründe olmayan bir AI entegrasyonu canlı ürün demosunda varmış gibi gösterilmemelidir.

---

## 9. Demo Videosu

**Video bağlantısı:**

TODO — Yoksa `Yok` yazın.

Video hazırlanırsa mümkün olduğunda:

- Gerçek çalışan ürünü göstermeli
- Final demo akışıyla uyumlu olmalı
- Hassas bilgi içermemeli
- Erişilebilirliği final teslimden önce kontrol edilmeli

> Büyük video dosyalarını gereksiz yere repository'ye eklemek yerine
> erişilebilir bir bağlantı kullanılabilir.
>
> Video bağlantısı `submission.json` içerisindeki `sunum.demo_akisi`
> alanının yerine geçmez.
>
> `demo_akisi`, gerçek sunum adımlarını anlatmalıdır.

---

## 10. Canlı Demo Yedek Planı

Canlı demo sırasında teknik bir problem yaşanması ihtimaline karşı
kritik çıktılar önceden kanıtlanabilir halde tutulmalıdır.

**Ana demo yöntemi:**

TODO

**Yedek kanıtlar:**

- [ ] Kritik ekran görüntüleri hazır
- [ ] X-Factor ekran görüntüsü hazır
- [ ] Gerçek sonuç / metrik görüntüsü hazır
- [ ] Gerekliyse kısa demo videosu hazır
- [ ] Çalıştırma komutu hazır
- [ ] Demo verisi hazır

> Yedek materyal, çalışmayan bir özelliği çalışıyormuş gibi göstermek için kullanılmamalıdır.
> Yalnızca daha önce gerçekten çalıştırılmış ve doğrulanmış çözümün kanıtı olmalıdır.

---

## 11. Canlı Demo Kontrolü

Sunumdan önce:

- [ ] Uygulama yeniden çalıştırıldı
- [ ] Final çalıştırma komutu doğrulandı
- [ ] Demo için gereken sentetik veri hazır
- [ ] Demo akışı baştan sona test edildi
- [ ] Demo sırasında gösterilecek ekranlar belirlendi
- [ ] Ekran görüntüleri gerçek ve güncel
- [ ] Gösterilecek sonuçlar doğrulandı
- [ ] Gösterilecek metrikler gerçek ölçümlere dayanıyor
- [ ] XAI kullanılıyorsa gerçek kanıta dayanıyor
- [ ] X-Factor gerçekten çalışıyor
- [ ] X-Factor kod referansı güncel
- [ ] Demo adımları `submission.json` ile tutarlı
- [ ] Demo anlatımı README / AI_JURI ile çelişmiyor
- [ ] Yedek demo kanıtları hazır
- [ ] Gizli bilgi görünmüyor
- [ ] API key / token görünmüyor
- [ ] Gerçek müşteri / production / kişisel veri görünmüyor
- [ ] Açık terminal veya ekranlarda hassas bilgi bulunmuyor

---

## 12. Güvenlik

Ekran görüntüsü, video veya canlı demo hazırlanmadan önce aşağıdaki bilgilerin
görünmediğinden emin olun:

```text
API key
Access token
Parola
Credential
Private key
Secret
Gizli connection string
Gerçek müşteri verisi
Production verisi
Kişisel veri
Hassas kurum içi bilgi
```

Hackathon çözümünde yalnızca etkinlik kapsamında izin verilen sentetik veri kullanılmalıdır.

Ekran görüntüsü alınmadan önce:

- Terminal çıktıları
- Browser sekmeleri
- `.env`
- IDE açık dosyaları
- URL parametreleri
- Bildirimler
- Kullanıcı / hesap bilgileri

de kontrol edilmelidir.

---

## 13. Sunumla İlişkisi

Canlı demo, çözümün gerçekten çalıştığını göstermek için kullanılmalıdır.

Önerilen anlatım mantığı:

```text
Problemi göster
      ↓
Girdiyi / durumu göster
      ↓
Çözümü çalıştır
      ↓
Gerçek sonucu göster
      ↓
Gerekçe / kanıtı göster
      ↓
X-Factor'ı göster
      ↓
Değeri tek cümlede özetle
```

Uzun teknik açıklamalar yerine mümkün olduğunca çalışan ürün ve gerçek kanıt merkeze alınmalıdır.

Teknik ayrıntılar gerekiyorsa:

- `docs/mimari.md`
- `src/README.md`
- `AI_JURI.md`

üzerinden desteklenebilir.

---

## 14. Final Tutarlılık Kontrolü

Final teslimden önce:

- [ ] Demo gerçek çalışan ürünü gösteriyor
- [ ] Demo akışı `submission.json` ile uyumlu
- [ ] Demo anlatımı `README.md` ile uyumlu
- [ ] Demo anlatımı `AI_JURI.md` ile uyumlu
- [ ] X-Factor aynı özelliği anlatıyor
- [ ] X-Factor kod kanıtı gerçek
- [ ] Ekran görüntüleri final ürünle uyumlu
- [ ] Metrikler diğer dokümanlarla tutarlı
- [ ] AI kullanımı abartılmıyor
- [ ] Kullanılmayan özellik demo içerisinde gösterilmiyor
- [ ] Hassas veya gizli veri bulunmuyor
- [ ] Gerekli `TODO` alanları final bilgilerle güncellendi