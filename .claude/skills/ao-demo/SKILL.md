---
name: ao-demo
description: Final repo kanıtlarından maksimum 7 dakikalık ürün ağırlıklı sunum ve istenirse offline HTML sunum hazırlar.
argument-hint: "[plan | html]"
disable-model-invocation: true
---

Mod: $ARGUMENTS

CLAUDE.md kurallarına uy.

1. README, AI_JURI, submission.json, demo/ ve gerçek ürünü temel al.
2. En fazla 7 dakika: 20 sn açılış; AI stratejisi/insan-AI iş bölümü; canlı demo; XAI; X-Factor; dürüst sınırlar; fallback; kapanış; 5 olası jüri sorusu.
3. Yalnız gerçek ölçüm/özellik kullan. Olmayan özellik veya başarı oranı uydurma.
4. Slayt değil çalışan ürün merkezli akış kur.
5. Mod "html" ise demo/CFDI_Final_Sunum.html oluştur: en fazla 4 ekran, 16:9, tek dosya, offline, harici CDN yok, ok tuşlarıyla geçiş. Gerçek screenshot varsa kullan; yoksa uydurma.
6. HTML sonrası temel yapıyı doğrula ve insan görsel kontrolü iste.
