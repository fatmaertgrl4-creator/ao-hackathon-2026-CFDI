---
name: ao-xfactor
description: Çözüm için uygulanabilir ve kanıtlanabilir X-Factor adaylarını değerlendirir; demo değeri, risk ve AI rolünü dengeler.
argument-hint: "[ürün bağlamı veya aday fikir]"
disable-model-invocation: true
---

Görev/bağlam: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. 2-4 gerçekçi X-Factor adayı değerlendir: kullanıcı değeri, demo etkisi, uygulanabilirlik, teknik risk, kanıtlanabilirlik, AI rolü.
2. Kazanan çıkarmak için zorlama. En iyi aday varsa gerekçesiyle öner.
3. Kritik operasyon kararını sırf "AI olsun" diye LLM'ye bırakma. Deterministik çözüm daha güvenliyse bunu açıkça söyle.
4. Seçilen aday için minimum implementasyon planını ve beklenen repo kanıt yollarını ver.
5. Olmayan özelliği varmış gibi anlatma. Kod değişikliği yalnız açıkça istenirse yapılır.
