# S-A1 — ALARM FIRTINASI

### AO Hackathon 2026 · Senaryo Brifingi · Teslim saati 17:30

## Sahne

Eylül ayının bir gecesi, saat 02 : 14. Operasyon merkezindeki alarm ekranı sessizce akmaya başlar, sonra hızlanır. Farklı izleme sistemlerinden, farklı servislerden, farklı şiddetlerde alarmlar birbirini kovalar. Nöbetçi mühendis ekrana baktığında iki saatlik pencerede binlerce satır görür.

O gece birden fazla şey aynı anda ters gitmiştir. Bazıları birbiriyle ilişkilidir, bazıları tamamen bağımsızdır; alarm ekranında hepsi yan yana akmaktadır.

## Çözülmesi Beklenen Problem

Nöbetçi mühendisin karşılaştığı asıl güçlük alarm sayısı değil, alarmlar arasındaki neden-sonuç ilişkisinin görünmez olmasıdır. Hangi alarmın kök neden, hangisinin türev etki, hangisinin ise tamamen alakasız gürültü olduğu ayırt edilemediği için müdahale sırası yanlış kurulur ve çözüm süresi uzar.

**Görev:** Alarm selini, nöbetçi mühendisin okuyup harekete geçebileceği birkaç karara indirgemek ve bu indirgemenin gerekçesini gösterebilmek.

## Zorunlu Gereksinimler

1. Verilen alarm akışının tamamını okuyup işleyebilmek.
2. Alarmları anlamlı gruplara indirgemek ve her grup için tek bir olay kartı üretmek.
3. Her olay kartında kök neden hipotezi, etkilenen servis listesi, alarm sayısı ve zaman aralığını göstermek.
4. Her kart için önerilen ilk aksiyonu üretmek ve bu aksiyonu sahip ile durum bilgisi içerecek şekilde kayıt altına almak.
5. Opsiyonel olarak bir aksiyonun açıldıktan sonra kapanana kadar izlenebildiğini demoda göstermek.

## Bonus Gereksinimler

- Kök neden hipotezinin neden bu olduğunu doğal dille açıklamak ve karşı olasılıkları belirtmek.
- Gürültü olarak elenen alarmların neden elendiğini gösteren bir denetim görünümü sunmak.
- Benzer geçmiş olay örüntülerini yakalayıp kartın üzerine iliştirmek.

## Kapsam Dışı

- Gerçek zamanlı akış işleme altyapısı kurmak gerekli değildir; dosyayı toplu okumak yeterlidir.
- Kullanıcı yönetimi, oturum açma ve yetkilendirme beklenmemektedir.
- Kalıcı veritabanı zorunlu değildir; bellek içi saklama kabul edilir.

## Kabul Kriterleri

- Uygulama, verilen veri paketiyle sıfırdan ayağa kalkıp sonuç üretir.
- 3.000 alarm, en fazla on beş olay kartına indirgenir.
- En az bir aksiyon demo sırasında açılıp durumu değiştirilerek gösterilebilir.
- Kök neden hipotezleri ekranda gerekçesiyle birlikte görülebilir.

## Başarı Nasıl Ölçülecek?

| Ölçüt | Ne bakılacak |
|---|---|
| İndirgeme oranı | Üretilen kart sayısının toplam alarm sayısına oranı |
| Kök neden isabeti | Doğrulama verisindeki gerçek köklerden kaçının yakalandığı |
| Yanlış birleştirme | Birbiriyle ilgisiz iki olayın tek karta konulup konulmadığı |
| Gürültü elemesi | Elenen alarmların ne kadarının gerçekten gürültü olduğu |

## Veri Sözlüğü Özeti

Bu paketteki tüm veriler sentetiktir. Hiçbir gerçek sistemden alınmamıştır ve hiçbir kurumsal sisteme erişim gerektirmez.

**Gözlem penceresi:** 10 Eylül 2026 Perşembe, 01:30-03:30  
**Toplam alarm:** 3.000  
**Servis:** 27  
**Sunucu:** 56  
**Bağımlılık kaydı:** 32

### Veri Dosyaları

| Dosya | Açıklama |
|---|---|
| `alarms.csv` / `alarms.json` | Alarm akışının tamamı |
| `service_dependencies.csv` | Servis bağımlılık grafiği |
| `host_inventory.csv` | Host, servis, lokasyon ve kritiklik envanteri |

### Önemli Alanlar

| Alan | Açıklama |
|---|---|
| `alarm_id` | Benzersiz alarm kimliği |
| `timestamp` | Alarmın üretildiği zaman |
| `source_system` | Alarmı üreten izleme sistemi |
| `host` | Sunucu adı |
| `service` | Alarmın ait olduğu servis |
| `severity` | 1-5 arası şiddet |
| `alarm_type` | Alarm tipi kodu |
| `message` | İnsan tarafından okunabilir alarm metni |
| `veri_merkezi`, `kabin`, `ortam` | Lokasyon ve ortam bilgisi |

### Bilinmesi Gerekenler

- Veri setinde birden fazla bağımsız gerçek olay vardır.
- Alarmların önemli bir bölümü arka plan gürültüsüdür.
- Bazı olaylar ani patlama şeklinde, bazıları uzun süreye yayılarak gelişir.
- Alarm tipleri olaylar arasında paylaşılır; tek başına alarm tipine bakarak ayrım yapmak yanıltıcıdır.
- Doğrulama verisi jüri değerlendirmesi sırasında açılacaktır.

## Uygulamada Karşılanan Maddeler

- `alarms.csv` içindeki 3.000 alarm işlendi.
- 7 olay kartı üretildi; bu, en fazla 15 kart kabul kriterinin altındadır.
- Her kartta kök neden hipotezi, servis listesi, alarm sayısı, zaman aralığı ve kanıt alanları bulunuyor.
- Aynı korelasyona ait alarm satırları kart içinde aynı grup altında gösteriliyor.
- `service_dependencies.csv` bağımlılık etkisi için, `host_inventory.csv` servis/host kritiklik bilgisi için kullanılıyor.
- Her kartta aksiyon, sahip ve durum bilgisi var.
- Demo API'si aksiyon durumunun değiştirilebildiğini gösteriyor.

## Bonus Kapsamı

- Kök neden hipotezi doğal dille açıklanıyor.
- Karşı olasılıklar kart üzerinde gösteriliyor.
- Gürültü olarak elenen alarmlar nedenleriyle denetim görünümünde listeleniyor.
- Benzer geçmiş örüntü notu veri içinde bulunabildiği ölçüde karta ekleniyor.
