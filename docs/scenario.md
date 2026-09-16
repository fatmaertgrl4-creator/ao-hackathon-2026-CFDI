# S-A1 — Alarm Fırtınası

## Kısa Senaryo

Eylül ayının bir gecesi operasyon merkezindeki alarm ekranında iki saatlik pencerede binlerce alarm oluşur. Farklı izleme sistemleri, farklı servisler ve farklı alarm tipleri aynı akışta görünür.

## Çözülmesi Beklenen Problem

Nöbetçi mühendisin alarm sayısını değil, alarmlar arasındaki neden-sonuç ilişkisini çözmesi gerekir. Hangi alarmın kök neden, hangisinin türev etki ve hangisinin gürültü olduğunu görünür hale getirmek beklenir.

## Zorunlu Gereksinimler

- Verilen alarm akışının tamamını okumak ve işlemek.
- Alarmları anlamlı gruplara indirgemek ve her grup için tek olay kartı üretmek.
- Her kartta kök neden hipotezi, etkilenen servis listesi, alarm sayısı ve zaman aralığını göstermek.
- Her kart için önerilen ilk aksiyonu sahip ve durum bilgisiyle kayıt altına almak.

## Uygulamada Karşılanan Maddeler

- `alarms.csv` içindeki 3.000 alarm işlendi.
- 7 olay kartı üretildi.
- Her kartta kök neden hipotezi, servis listesi, alarm sayısı, zaman aralığı ve kanıt alanları bulunuyor.
- Her kartta aksiyon, sahip ve durum bilgisi var.
- Demo API'si aksiyon durumunun değiştirilebildiğini gösteriyor.

## Bonus Kapsamı

- Kök neden hipotezi doğal dille açıklanıyor.
- Karşı olasılıklar kart üzerinde gösteriliyor.
- Gürültü olarak elenen alarmlar nedenleriyle denetim görünümünde listeleniyor.
- Benzer geçmiş örüntü notu veri içinde bulunabildiği ölçüde karta ekleniyor.
