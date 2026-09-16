# GitHub Copilot Instructions

Bu projede geliştirme asistanı olarak GitHub Copilot kullanılmıştır.

## Kullanım kapsamı

- Bu proje GitHub Copilot Chat ile geliştirildi.
- Copilot; senaryo analizi, algoritma taslağı, kod geliştirme ve dokümantasyon desteğinde kullanıldı.
- Kritik sonuçlar, metrikler ve dokümantasyon çıktıları insan tarafından doğrulandı.
- Ürünün runtime'ında canlı LLM veya OpenAI API çağrısı bulunmuyor.

## Genel geliştirme kuralları

- Önce mevcut repo yapısını ve ilgili dosyaları incele.
- Yalnızca verilen görev için gerekli dosyalarda değişiklik yap.
- İlgisiz refactor veya mimari değişiklik yapma.
- `src/app.py` üzerinde gereksiz refactor yapma.
- Mevcut proje yapısını ve isimlendirmeleri koru.
- Gerçek metrikleri değiştirme veya uydurma.
- Kök nedenleri doğrulanmış gerçekler gibi değil, hipotez olarak ifade et.
- Yeni dependency eklemeden önce gerçekten gerekli olup olmadığını kontrol et.
- Test çalıştırılmadıysa başarılı olmuş gibi gösterme.
- Yapılan değişikliklerden sonra:
  - değiştirilen dosyaları,
  - yapılan değişiklikleri,
  - test komutlarını,
  - beklenen sonucu,
  - insan kontrolü gereken noktaları
  açıkça belirt.

## Proje yaklaşımı

Geliştirme MVP odaklı yürütülmüştür.

Her modül ayrı görev olarak ele alınmış ve yalnızca ihtiyaç duyulan kapsam geliştirilmiştir.

## Not

Root'taki `copilot-instructions.md` yarışma sürecinde oluşan geliştirme izini korumak için saklanmaktadır. GitHub Copilot'un standart konumu ayrıca `.github/copilot-instructions.md` olarak eklenmiştir.
