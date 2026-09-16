# S-A1 — ALARM FIRTINASI
### AO Hackathon 2026 · Senaryo Brifingi · Teslim saati 17:30

---

## Sahne

Eylül ayının bir gecesi, saat 02 : 14. Operasyon merkezindeki alarm ekranı
sessizce akmaya başlar, sonra hızlanır. Farklı izleme sistemlerinden, farklı
servislerden, farklı şiddetlerde alarmlar birbirini kovalar. Nöbetçi mühendis
ekrana baktığında iki saatlik pencerede binlerce satır görür.

O gece birden fazla şey aynı anda ters gitmiştir. Bazıları birbiriyle
ilişkilidir, bazıları tamamen bağımsızdır; alarm ekranında hepsi yan yana
akmaktadır.

## Çözülmesi beklenen problem

Nöbetçi mühendisin karşılaştığı asıl güçlük alarm sayısı değil, alarmlar
arasındaki neden-sonuç ilişkisinin görünmez olmasıdır. Hangi alarmın kök neden,
hangisinin türev etki, hangisinin ise tamamen alakasız gürültü olduğu ayırt
edilemediği için müdahale sırası yanlış kurulur ve çözüm süresi uzar.

**Göreviniz:** Alarm selini, nöbetçi mühendisin okuyup harekete geçebileceği
birkaç karara indirgemek ve bu indirgemenin gerekçesini gösterebilmek.

---

## Zorunlu gereksinimler

1. Verilen alarm akışının **tamamını** okuyup işleyebilmek. Kısmi veri ile
   çalışan çözümler eksik sayılır.
2. Alarmları anlamlı gruplara indirgemek ve her grup için **tek bir olay kartı**
   üretmek.
3. Her olay kartında kök neden hipotezi, etkilenen servis listesi, alarm sayısı
   ve zaman aralığını göstermek.
4. Her kart için önerilen ilk aksiyonu üretmek ve bu aksiyonu **sahip ile durum
   bilgisi** içerecek şekilde kayıt altına almak.
5. *(Opsiyonel)* Bir aksiyonun açıldıktan sonra kapanana kadar **izlenebildiğini**
   demoda göstermek. Yapılması durumunda çözümünüze güç katar.

## Bonus gereksinimler (X-Factor alanı)

- Kök neden hipotezinin neden bu olduğunu doğal dille açıklamak ve **karşı
  olasılıkları** da belirtmek.
- Gürültü olarak elenen alarmların **neden elendiğini** gösteren bir denetim
  görünümü sunmak.
- Benzer geçmiş olay örüntülerini yakalayıp kartın üzerine iliştirmek.

## Kapsam dışı

- Gerçek zamanlı akış işleme altyapısı kurmak gerekli değildir; dosyayı toplu
  okumak yeterlidir.
- Kullanıcı yönetimi, oturum açma ve yetkilendirme beklenmemektedir.
- Kalıcı veritabanı zorunlu değildir; bellek içi saklama kabul edilir.

---

## Kabul kriterleri (kendi kendinizi denetleyin)

- [ ] Uygulama, verilen veri paketiyle sıfırdan ayağa kalkıp sonuç üretiyor
- [ ] 3.000 alarm, en fazla on beş olay kartına indirgenmiş durumda
- [ ] *(Opsiyonel)* En az bir aksiyon demo sırasında açılıp durumu değiştirilerek gösteriliyor
- [ ] Kök neden hipotezleri ekranda gerekçesiyle birlikte görülebiliyor

## Başarınız nasıl ölçülecek

| Ölçüt | Ne bakılacak |
|---|---|
| İndirgeme oranı | Ürettiğiniz kart sayısının toplam alarm sayısına oranı |
| Kök neden isabeti | Doğrulama verisindeki gerçek köklerden kaçını yakaladığınız |
| Yanlış birleştirme | Birbiriyle ilgisiz iki olayı tek karta koyup koymadığınız |
| Gürültü elemesi | Elenen alarmların ne kadarının gerçekten gürültü olduğu |

---

## Peşin yanıtlanan sorular

**Alarmların hepsini kullanmak zorunda mıyız?**
Evet. Veri setinin tamamı işlenmelidir; örnekleme yaparsanız demoda belirtin.

**Kök nedeni bulamazsak sıfır mı alırız?**
Hayır. Doğru gerekçelendirilmiş yanlış hipotez, gerekçesiz doğru hipotezden daha
yüksek puan alabilir.

**Hazır korelasyon kütüphanesi kullanabilir miyiz?**
Evet, tüm açık kaynak kütüphaneler serbesttir. Kullandığınız her kütüphaneyi
README dosyanızda belirtin.

**Arayüz web olmak zorunda mı?**
Hayır. Terminal, masaüstü veya web fark etmez; ancak demoda canlı çalışması gerekir.

**Kaç tane gerçek olay var?**
Söylenmeyecektir. Bunu veriden çıkarmak senaryonun bir parçasıdır.

---

## Teslim

Repo adresiniz başvuru sırasında alınmıştır; ayrıca bir gönderim yapmanıza gerek
yoktur. Değerlendirme **17:30'daki son commit** üzerinden yapılacaktır.
Reponuz public olmalıdır.

Repo şunları içermelidir: `README.md` (kurulum, kullanılan AI araçları, MCP listesi,
ekran görüntüleri), `docs/` klasörü (plan, fazlar, mimari), `.env.example` ve
AI yapılandırma dosyalarınız (`CLAUDE.md`, `.cursorrules`, `copilot-instructions.md`).

Sorularınız için önce takım mentörünüze başvurun.


## Veri Sözlüğü
# S-A1 "Alarm Fırtınası" — Veri Sözlüğü

Bu paketteki tüm veriler **sentetiktir**. Hiçbir gerçek sistemden alınmamıştır,
hiçbir kurumsal sisteme erişim gerektirmez.

**Gözlem penceresi:** 10 Eylül 2026 Perşembe, 01:30 – 03:30 (2 saat)
**Toplam alarm:** 3.000 · **Servis:** 27 · **Sunucu:** 56 · **Bağımlılık kaydı:** 32

---

## alarms.json

Alarm akışının tamamı. JSON dizisi; her eleman bir alarm kaydı.

| Alan | Tip | Açıklama |
|---|---|---|
| `alarm_id` | metin | Benzersiz alarm kimliği (`ALM-00001`) |
| `timestamp` | ISO-8601 | Alarmın üretildiği an (`2026-11-21T01:42:17`) |
| `source_system` | metin | Alarmı üreten izleme sistemi: OBM, Prometheus, Zabbix, AppDynamics, SyslogNG |
| `host` | metin | Sunucu adı (`ao-014-billing`) |
| `service` | metin | Alarmın ait olduğu servis |
| `severity` | tamsayı 1–5 | 1 = bilgi, 2 = uyarı, 3 = küçük, 4 = büyük, 5 = kritik |
| `alarm_type` | metin | Alarm tipi kodu (aşağıdaki tabloya bakınız) |
| `message` | metin | İnsan tarafından okunabilir alarm metni |
| `tags` | nesne | `veri_merkezi`, `kabin`, `ortam` anahtarlarını içerir |

## alarms.csv

Aynı verinin düz tablo hâli. `tags` nesnesi üç ayrı sütuna açılmıştır
(`veri_merkezi`, `kabin`, `ortam`). JSON ile CSV arasında **içerik farkı yoktur**;
hangisiyle çalışacağınız sizin tercihinizdir.

## service_dependencies.csv

| Alan | Açıklama |
|---|---|
| `kaynak_servis` | Bağımlı olan servis |
| `hedef_servis` | Bağımlı olunan servis |
| `bagimlilik_tipi` | `senkron` veya `asenkron` |
| `kritiklik` | Hedef servisin iş kritikliği |

**Okuma yönü:** `kaynak_servis`, `hedef_servis`e bağımlıdır. Yani `hedef_servis`
bozulursa `kaynak_servis` etkilenir.

## host_inventory.csv

| Alan | Açıklama |
|---|---|
| `host` | Sunucu adı |
| `servis` | Sunucu üzerinde koşan servis |
| `veri_merkezi` | `dc1` veya `dc2` |
| `kabin` | `rack-A`, `rack-B` veya `rack-C` |
| `ortam` | Tümü `prod` |
| `is_kritikligi` | `kritik`, `yuksek`, `orta`, `dusuk` |

---

## Alarm tipi kodları

| Kod | Anlamı |
|---|---|
| `network_down` | Arayüz bağlantısı koptu |
| `network_flap` | Link durumu tekrar tekrar değişiyor |
| `pkt_loss` | Paket kaybı |
| `timeout` | Bağımlı servise yapılan çağrı zaman aşımına uğradı |
| `conn_refused` | Bağlantı reddedildi |
| `http_5xx` | Sunucu hata oranı eşiği aştı |
| `latency_high` | Yanıt süresi p99 eşiği aştı |
| `disk_full` | Disk kritik seviyede dolu |
| `disk_warn` | Disk uyarı seviyesinde |
| `db_write_fail` | Veritabanı yazma hatası |
| `db_conn_pool` | Bağlantı havuzu tükendi |
| `mem_high` | Bellek kullanımı yüksek |
| `gc_pressure` | Çöp toplama duraklaması uzun |
| `oom_risk` | Bellek tükenmesi riski |
| `ext_unreach` | Dış servis erişilemiyor |
| `ext_slow` | Dış servis yavaş |
| `txn_fail` | İşlem başarısız |
| `queue_backlog` | Kuyruk birikimi |
| `batch_overlap` | Toplu iş penceresi çakışması |
| `batch_slow` | Toplu iş uzun sürüyor |
| `cpu_high` | CPU kullanımı yüksek |
| `cert_expiry` | Sertifika süresi dolmak üzere |
| `backup_warn` | Yedekleme gecikmeli |
| `ntp_drift` | Saat sapması |
| `log_rotate` | Log rotasyonu uzun sürdü |
| `thread_pool` | İş parçacığı havuzu doluluğu |

---

## Bilinmesi gerekenler

- Veri setinde **birden fazla bağımsız gerçek olay** vardır. Kaç tane olduğu
  size söylenmeyecektir.
- Alarmların önemli bir bölümü **arka plan gürültüsüdür**: herhangi bir olayla
  ilgisi yoktur ve hiçbir aksiyona yol açmaz.
- Bazı olaylar ani patlama şeklinde, bazıları **uzun süreye yayılarak** gelişir.
  İkincisini yakalamak birincisinden zordur.
- Alarm tipleri olaylar arasında **paylaşılır**. Tek başına alarm tipine bakarak
  ayrım yapmak yanıltıcıdır.
- Doğrulama verisi (hangi alarmın hangi olaya ait olduğu) **jüriye değerlendirme
  aşamasında** açılacaktır.
