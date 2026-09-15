---
name: ao-xai
description: Çözümün açıklanabilirliğini gerçek kanıtlara bağlar; gerekçe, kanıt, çelişen kanıt, belirsizlik ve sonraki kontrolü değerlendirir.
argument-hint: "[XAI görevi veya hedef dosya]"
disable-model-invocation: true
---

Görev: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. Mevcut analiz çıktısını ve ilgili UI/kanıt kodunu incele.
2. Açıklama mümkünse şu alanları kapsasın: sonuç, gerekçe, destekleyen kanıt, çelişen kanıt, confidence, uncertainty, next_check.
3. Her açıklamayı gerçek veri/hesap çıktısına bağla. Kanıt yoksa "yok/tespit edilmedi" de; uydurma.
4. Confidence kalibre edilmiş olasılık değilse yüzde gibi sunma.
5. Root cause doğrulanmadıysa doğrulanmış gibi yazma.
6. Kod değişikliği istenirse minimum değişiklik yap ve gerçek testle doğrula.
