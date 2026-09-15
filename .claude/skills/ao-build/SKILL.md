---
name: ao-build
description: İstenen tek modülü veya küçük değişikliği minimum kapsamda geliştirir ve gerçek test komutuyla doğrular.
argument-hint: "[modül veya görev]"
disable-model-invocation: true
---

Görev: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. Yalnız gerekli dosyaları incele.
2. Değişiklik gerekiyorsa önce hedef dosyaları ve planı en fazla 5 maddede söyle. Kullanıcı zaten açıkça uygulamayı istemediyse onay bekle.
3. Yalnız istenen işi yap; ilgisiz refactor/özellik ekleme.
4. Mevcut çalışan akışı koru. Yeni dependency gerekiyorsa requirements/dependency kaydını güncelle.
5. Gerçek test çalıştır. "Çalışıyor" demek için test komutunu, exit sonucunu ve önemli çıktıyı raporla.
6. Test başarısızsa önce en küçük düzeltmeyi öner/uygula; kapsamı büyütme.
7. Destructive Git işlemi yapma.
