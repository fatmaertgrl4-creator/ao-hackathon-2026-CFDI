# AI Jüri Özeti

> **DURUM: TASLAK — teslim edilebilir değil.**
> Başlık yapısı şartnameye göre sabitlenmiştir; **sırayı ve başlıkları değiştirmeyin.**
> Her `TODO` doldurulmalı ve her iddianın altına **gerçek bir dosya yolu** yazılmalıdır.
> Kanıtsız iddia puanlanmaz — var olmayan bir dosyaya referans vermek iddiayı çürütür.
> Takım: **CFDI** · Repo: https://github.com/fatmaertgrl4-creator/ao-hackathon-2026-CFDI

---

## 1. AI Stratejimiz ve İş Akışı

Hangi AI aracını hangi işte kullandık, hangi kararı insan verdi.

TODO — Şunları somut yazın:
- Hangi araç (Claude Code / Cursor / Copilot / SAKA) hangi iş için kullanıldı?
- İnsanın verdiği kararlar neler? (mimari seçimi, kapsam, kabul kriteri, kod incelemesi)
- Modele bırakılan işler neler? (boilerplate, test yazımı, refactor, hata ayıklama)
- İş akışınız nasıldı? (örn. insan spec yazar → model taslak üretir → insan inceler → test)

**Doğrulanabilir mevcut durum:** Depo yönetimi ve doküman iskelesi Claude Code ile yapıldı;
araç erişimi `testgencer.txt` ile doğrulandı, ajan talimatları `CLAUDE.md` içinde tutuluyor.

**Kanıt:** [prompts/](prompts/) · [CLAUDE.md](CLAUDE.md) · [docs/plan.md](docs/plan.md)

---

## 2. Problemi Nasıl Çözdük

Yaklaşımımız, ürettiğimiz çıktı ve ölçtüğümüz sonuç.

TODO — Şu üçünü ayrı ayrı yazın:
- **Yaklaşım:** Problemi nasıl parçaladınız, hangi yolu seçtiniz?
- **Çıktı:** Ortaya ne çıktı? Hangi modüller çalışıyor?
- **Ölçtüğünüz sonuç:** Sayı verin (doğruluk, süre, işlenen kayıt, token maliyeti...).
  Ölçmediyseniz "ölçmedik" yazın; uydurulmuş metrik en ağır kayıptır.

**Kanıt:** [src/](src/) · [docs/mimari.md](docs/mimari.md) · [demo/](demo/)

---

## 3. X-Factor

Sıradan bir çözümün yapamayacağı **tek** şey ve nerede yaptığımız.

TODO — Tek bir şey seçin, liste yapmayın. "Şunu da yaptık" eklemek iddiayı zayıflatır.
Ardından tam olarak nerede olduğunu gösterin.

**Kanıt:** `src/<dosya>:<satır aralığı>` — TODO: gerçek dosya ve satır aralığıyla değiştirin.

---

## 4. Çalıştırma

Tek komutla nasıl çalıştırılır, hangi çıktıyı üretir.

**Ön koşullar:** TODO

**Kurulum:**
```bash
TODO
```

**Tek komut:**
```bash
TODO
```

**Beklenen çıktı:** TODO — Ne göreceğini yazın; jüri bunu birebir çalıştıracak.

> Teslimden önce bu adımları **temiz bir dizinde sıfırdan** deneyin.
> Sizde çalışan ama jüride çalışmayan kurulum, puan kaybının en yaygın sebebidir.

**Kanıt:** [README.md](README.md) · [.env.example](.env.example)

---

## 5. Bilinen Sınırlar

Neyi yapamadık, neden. Dürüstlük puan kazandırır.

TODO — Somut yazın. Örnek biçim:
- **Yapamadık:** ... · **Neden:** ... · **Nasıl yapılırdı:** ...

**Bugün itibarıyla bilinen sınır:** Depoda henüz kaynak kod yok; bu dosya taslak
durumundadır ve 1–3. bölümler doldurulmamıştır.

**Kanıt:** [docs/fazlar.md](docs/fazlar.md)
