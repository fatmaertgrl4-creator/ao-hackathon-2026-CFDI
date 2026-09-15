---
name: ao-compare
description: Aynı görev ve aynı bağlamla elde edilmiş iki gerçek model çıktısını tarafsız karşılaştırır.
argument-hint: "[görev + Model A/B çıktıları veya dosyaları]"
disable-model-invocation: true
---

Karşılaştırma girdisi: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. Yalnız aynı görev ve yeterince aynı bağlamla üretilmiş GERÇEK iki çıktı varsa karşılaştır.
2. Gerçek model adı/sürümü yoksa uydurma; eksikliği belirt.
3. Kriterler: doğruluk, veriye dayanma, hallucination/aşırı çıkarım riski, açıklanabilirlik, uygulanabilirlik, karmaşıklık, operasyonel değer.
4. Ground truth yoksa doğruluk için "PUANLANAMAZ" yaz.
5. Kazanan çıkarmak için zorlama. Kanıt eşitse/eğer yetersizse söyle.
6. Sonunda insan için nihai karar önerisini kısa gerekçeyle ver.
7. Simülasyon/prova çıktısını gerçek yarışma kanıtı olarak kabul etme.
