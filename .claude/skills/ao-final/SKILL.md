---
name: ao-final
description: Final dokümantasyonu gerçek repo kanıtlarıyla hazırlar veya teslim öncesi salt-okunur audit yapar.
argument-hint: "[prepare | audit]"
disable-model-invocation: true
---

Mod: $ARGUMENTS

CLAUDE.md kurallarına uy.

PREPARE ise:
- README.md, AI_JURI.md, submission.json, docs/, demo/ ve prompts/used içeriğini yalnız doğrulanabilir bilgilerle hizala.
- Bilinmeyen takım/model/sürüm/iletişim bilgisini uydurma; HUMAN INPUT REQUIRED bırak.
- Alarm deterministikse öyle yaz; runtime AI yoksa varmış gibi gösterme.
- Ölçülmemiş başarı metriği ekleme.
- submission.json'u gerçek JSON doğrulamasıyla kontrol et.

AUDIT ise (veya mod belirtilmemişse):
- Dosya değiştirme.
- README, AI_JURI, submission, CLAUDE, docs, prompts, src, demo, .env.example, .gitignore ve çalışan kod tutarlılığını denetle.
- Model sürümü, prompts/used, X-Factor/XAI kod kanıtı, ölçülmüş metrik, MCP/API, TODO, secret, demo, bilinen sınırlar ve run komutunu kontrol et.
- prompts/templates ve prompts/_SABLON.md içindeki bilinçli placeholder'ları hata sayma.
- Son satır yalnız READY, NOT READY veya INSUFFICIENT EVIDENCE olsun. NOT READY ise önce kritik eksikleri sırala.
- Destructive Git işlemi yapma.
