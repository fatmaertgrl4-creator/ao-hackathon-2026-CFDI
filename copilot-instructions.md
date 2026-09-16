# GitHub Copilot Instructions

Bu projede geliştirme asistanı olarak GitHub Copilot kullanılmıştır.

## Genel geliştirme kuralları

- Önce mevcut repo yapısını ve ilgili dosyaları incele.
- Yalnızca verilen görev için gerekli dosyalarda değişiklik yap.
- İlgisiz refactor veya mimari değişiklik yapma.
- Mevcut proje yapısını ve isimlendirmeleri koru.
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
