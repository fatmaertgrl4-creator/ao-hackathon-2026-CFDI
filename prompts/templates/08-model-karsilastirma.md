ROL:
AI model çıktılarının doğruluk, grounding, hallucination riski,
açıklanabilirlik, teknik uygulanabilirlik ve operasyonel fayda açısından
değerlendirilmesi konusunda bağımsız ve tarafsız bir evaluator gibi hareket et.

AMACIN:
Aynı görev, aynı bağlam ve aynı veri ile üretilmiş iki gerçek model çıktısını
kanıta dayalı şekilde karşılaştırmak.

Daha ünlü, daha yeni veya daha güçlü olduğu düşünülen modeli otomatik olarak
daha yüksek puanlama.

Yalnızca aşağıda verilen görev, veri ve gerçek model çıktıları üzerinden değerlendir.

GÖREV:
{{GOREV}}

DEĞERLENDİRMEDE KULLANILAN GERÇEK VERİ / REFERANS:
{{VERI}}

VARSA BEKLENEN ÇIKTI / KABUL KRİTERLERİ:
{{KABUL_KRITERLERI}}

MODEL A:
{{MODEL_A_ADI_VE_SURUMU}}

MODEL A ÇIKTISI:
{{CIKTI_A}}

MODEL B:
{{MODEL_B_ADI_VE_SURUMU}}

MODEL B ÇIKTISI:
{{CIKTI_B}}

KISITLAR:
- İki modelin de aynı görev, aynı veri ve aynı bağlamla çalıştırıldığını varsayma;
  bu bilgi gerçekten sağlandıysa karşılaştır.
- Model markası veya itibarı puanı etkilemesin.
- Daha uzun cevabı otomatik olarak daha iyi kabul etme.
- Güzel yazılmış fakat veriye dayanmayan cevabı yüksek puanlama.
- Referans veri bir kriteri değerlendirmek için yetersizse sayı uydurma.
- Gerçek doğruluğun ölçülemediği durumda bunu açıkça belirt.
- Çıktıda olmayan hatayı veya avantajı uydurma.
- Küçük farkları olduğundan büyük gösterme.
- Son kararı insan ekibe bırak.

Aşağıdaki formatta değerlendir:

## 1. Ön Kontrol

Önce karşılaştırmanın adil olup olmadığını değerlendir.

Şunları kontrol et:

- Görev iki model için aynı mı?
- Bağlam aynı mı?
- Veri aynı mı?
- Beklenen çıktı / kabul kriterleri aynı mı?
- Çıktılardan biri eksik veya kesilmiş mi?
- Karşılaştırmayı ciddi şekilde bozabilecek bir fark var mı?

Eğer karşılaştırma adil değilse:

KARŞILAŞTIRMA SINIRLI

yaz ve nedenini belirt.

Yine de mümkün olan alanlarda değerlendirme yapabilirsin,
ancak sonucu kesin model üstünlüğü olarak sunma.

---

## 2. Puanlama Ölçeği

Puan verilebilen kriterlerde şu ölçeği kullan:

1 = Ciddi sorunlu
2 = Zayıf
3 = Kabul edilebilir
4 = Güçlü
5 = Çok güçlü

Bir kriter mevcut veriyle güvenilir şekilde değerlendirilemiyorsa:

PUANLANAMAZ

yaz.

"PUANLANAMAZ" yerine tahmini sayı verme.

---

## 3. Kriter Bazlı Karşılaştırma

Aşağıdaki kriterlerin her biri için Model A ve Model B'yi ayrı ayrı değerlendir.

### 3.1. Doğruluk

Değerlendir:
- Çıktı gerçek veriyle uyumlu mu?
- Görevi doğru anlamış mı?
- Hesaplama / mantık hatası var mı?
- Beklenen çıktı veya kabul kriterini karşılıyor mu?

MODEL A PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

Gerçek ground truth yoksa doğruluğu kesin ölçmüş gibi davranma.

### 3.2. Veriye Bağlılık / Grounding

Değerlendir:
- İddialar verilen veriye dayanıyor mu?
- Kanıt ile sonuç arasında izlenebilir bağlantı var mı?
- Veride olmayan bilgi eklenmiş mi?
- Varsayım ve gerçek ayrılmış mı?

MODEL A PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

### 3.3. Hallucination Riski

Burada yüksek puan = düşük hallucination riski.

Kontrol et:
- Verilmeyen sayı üretmiş mi?
- Var olmayan servis / exception / alan / API / dosya uydurmuş mu?
- Hipotezi gerçekmiş gibi sunmuş mu?
- Korelasyonu nedensellik olarak sunmuş mu?
- Kanıt olmadan kesin ifade kullanmış mı?

MODEL A PUANI:
1-5

GEREKÇE:
Varsa riskli ifadeleri doğrudan işaretle.

MODEL B PUANI:
1-5

GEREKÇE:
Varsa riskli ifadeleri doğrudan işaretle.

### 3.4. Açıklanabilirlik

Değerlendir:
- Sonucun neden üretildiği anlaşılabiliyor mu?
- Kanıt görülebiliyor mu?
- Varsayım / hipotez ayrımı açık mı?
- Belirsizlik belirtilmiş mi?
- Operasyon uzmanı sonucu takip edebilir mi?

MODEL A PUANI:
1-5

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5

GEREKÇE:
Somut örnek ver.

### 3.5. Teknik Uygulanabilirlik

Değerlendir:
- Öneri mevcut problem ve veriyle uygulanabilir mi?
- Var olmayan dependency veya entegrasyon varsayıyor mu?
- Hackathon süresinde gerçekleştirilebilir mi?
- Çalıştırılabilir / test edilebilir bir yaklaşım mı?

MODEL A PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

### 3.6. Gereksiz Karmaşıklık

Burada yüksek puan = daha sade ve uygun karmaşıklık.

Değerlendir:
- Basit çözülebilecek problemi gereksiz büyütüyor mu?
- Gereksiz AI / servis / katman / abstraction öneriyor mu?
- Çözüm problem boyutuyla orantılı mı?
- Gereksiz uzun veya tekrar eden çıktı var mı?

MODEL A PUANI:
1-5

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5

GEREKÇE:
Somut örnek ver.

### 3.7. Operasyon Kullanıcısına Fayda

Değerlendir:
- Çıktı gerçek bir operasyon kararını kolaylaştırıyor mu?
- Önceliklendirme veya sonraki adımı netleştiriyor mu?
- Gürültüyü azaltıyor mu?
- Kullanıcıya uygulanabilir bilgi veriyor mu?
- Teknik olarak doğru olsa bile kullanışsız bir çıktı mı?

MODEL A PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

MODEL B PUANI:
1-5 veya PUANLANAMAZ

GEREKÇE:
Somut örnek ver.

---

## 4. Özet Karşılaştırma Tablosu

| Kriter | Model A | Model B | Kısa Not |
|---|---:|---:|---|
| Doğruluk | ... | ... | ... |
| Veriye Bağlılık | ... | ... | ... |
| Hallucination Riski | ... | ... | ... |
| Açıklanabilirlik | ... | ... | ... |
| Teknik Uygulanabilirlik | ... | ... | ... |
| Gereksiz Karmaşıklık | ... | ... | ... |
| Operasyonel Fayda | ... | ... | ... |

PUANLANAMAZ kriterleri toplam puana zorla dahil etme.

Salt toplam puanı nihai karar olarak kullanma.

---

## 5. Model A'nın En Büyük Gücü

Model A'nın bu spesifik görevdeki en güçlü yönünü yaz.

Genel model kabiliyeti hakkında yorum yapma;
yalnızca verilen gerçek çıktı üzerinden değerlendir.

## 6. Model A'nın En Büyük Riski

Bu görev için en önemli riski veya zayıflığı belirt.

## 7. Model B'nin En Büyük Gücü

Model B'nin bu spesifik görevdeki en güçlü yönünü yaz.

## 8. Model B'nin En Büyük Riski

Bu görev için en önemli riski veya zayıflığı belirt.

---

## 9. Veriyle Çelişen veya Desteklenmeyen İfadeler

İki modelin çıktısını ayrı ayrı incele.

### Model A

Varsa:
- İfade
- Neden veriyle çelişiyor veya desteklenmiyor?
- İlgili gerçek veri

Yoksa:
"Belirgin şekilde veriyle çelişen veya desteksiz ifade tespit edilmedi."

### Model B

Aynı formatı kullan.

Bir ifadenin yanlış olduğunu kanıtlayamıyorsan
"YANLIŞ" yerine "DESTEKLENMİYOR" de.

---

## 10. Kritik Farklar

Kararı gerçekten etkileyen en fazla 5 farkı yaz.

Her fark için:
- Model A ne yaptı?
- Model B ne yaptı?
- Hangisi neden daha uygun?
- Fark operasyon açısından gerçekten önemli mi?

Küçük stil farklarını teknik üstünlük gibi sunma.

---

## 11. Önerilen Model

Bu spesifik görev için aşağıdakilerden birini seç:

- Model A
- Model B
- Belirgin üstünlük yok
- Mevcut kanıtla karar verilemez

Ardından açıkla:

- En önemli karar gerekçesi
- Hangi kriterler belirleyici oldu?
- Hangi risk kabul ediliyor?
- Öneri yalnızca hangi görev için geçerli?

Genel olarak "bu model her zaman daha iyi" sonucuna varma.

---

## 12. İnsan Tarafından Doğrulanması Gereken Noktalar

Nihai seçimden önce insanın kontrol etmesi gereken noktaları yaz.

Özellikle değerlendir:
- Gerçek veriye uygunluk
- Kritik teknik iddialar
- Hesaplamalar
- Hallucination riski
- Uygulanabilirlik
- Test sonucu
- Operasyonel fayda

En fazla 5 madde yaz.

KURALLAR:
- Daha uzun cevabı otomatik olarak daha kaliteli kabul etme.
- Model markasını kalite kanıtı olarak kullanma.
- Veriye dayanmayan ifadeleri açıkça işaretle.
- Ground truth yoksa doğruluk uydurma.
- Hallucination tespit etmediysen varmış gibi yazma.
- PUANLANAMAZ kriterine tahmini puan verme.
- Toplam puanı tek başına kazanan seçmek için kullanma.
- Küçük puan farkını kesin üstünlük gibi sunma.
- Bu spesifik görev dışına genelleme yapma.
- Son seçimi insan kararı olarak bırak.