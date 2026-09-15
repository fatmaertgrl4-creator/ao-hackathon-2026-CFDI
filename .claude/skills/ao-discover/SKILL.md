---
name: ao-discover
description: Hackathon senaryosunu ve sentetik veriyi kanıt odaklı analiz eder; problem, önemli sinyaller, hipotezler ve minimum MVP mimarisini çıkarır.
argument-hint: "[senaryo ve/veya veri yolu]"
disable-model-invocation: true
---

Görev/bağlam: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. Senaryoyu, ilgili veriyi ve gerekli repo yapısını incele. Dosya değiştirme.
2. Kısa çıktı ver: Problem, başarı kriteri, doğrulanmış kanıtlar, hipotezler, belirsizlikler, minimum MVP mimarisi, sonraki tek adım.
3. Kanıt ile yorumu ayır. Kanıtsız root cause ilan etme; korelasyonu nedensellik gibi sunma.
4. Tüm veriyi dökmek yerine anlamlı sinyalleri öne çıkar. Ölçülmemiş metrik uydurma.
5. Veri yeterliyse gereksiz soru sorma. Bloklayan eksik varsa tek kısa soru sor.
6. Kod yazma veya ürün dosyalarını değiştirme.
