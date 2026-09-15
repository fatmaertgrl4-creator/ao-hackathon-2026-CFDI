---
name: ao-redteam
description: Mevcut çözümü bağımsız senior SRE/tester gözüyle kırmaya çalışır; kritik hata, risk ve doğrulama açıklarını önceliklendirir.
argument-hint: "[inceleme kapsamı; boşsa tüm repo]"
disable-model-invocation: true
---

Kapsam: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. Repo, veri akışı, çalışan çözüm ve dokümantasyonu bağımsız tester gibi incele. Dosya değiştirme.
2. Özellikle kontrol et: ana problem, hesap doğruluğu, edge case, hata yönetimi, hallucination, kanıt/XAI grounding, yanlış alarm riski, demo kırılma noktaları.
3. Her bulguyu DOĞRULANMIŞ HATA / RİSK / DOĞRULAMA GEREKİYOR olarak sınıflandır; önem derecesi ve kanıt yolunu yaz.
4. En kritik 3 konuyu sırala ve en küçük düzeltmeyi öner.
5. Kanıt yoksa hata ilan etme. Büyük refactor önerme.
6. Sonraki düzeltmeler için /ao-build kullanılabilir.
