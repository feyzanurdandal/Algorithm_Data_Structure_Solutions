Senaryo üzerinde hash table mantığı nedir?

### **1. Gerçek Hayat Analojisi: Vestiyer vs. Dağınık Oda**

**Senaryo:** Bir düğündesin ve ceketini teslim edeceksin.

- **Dizi (Array) Mantığı (Yavaş):** Ceketlerin hepsini bir odaya rastgele attıklarını düşün. Ceketini geri almak istediğinde görevli içeri girer, en baştan başlar ve senin ceketini bulana kadar her ceketi tek tek kontrol eder. Oda ne kadar büyükse (n eleman), bulması o kadar uzun sürer. Bu **O(n)** süredir.
- **Hash Mantığı (Hızlı):** Ceketini teslim ettiğinde görevli sana bir **numara (anahtar)** verir ve ceketi o numaralı askıya asar. Sen geri geldiğinde numarayı verirsin, görevli hiç aramadan direkt o numaralı askıya gider ve ceketi alır. Odada 1000 tane de ceket olsa, senin ceketinin yeri bellidir. Tek hamlede alır. Bu **O(1)** süredir.

**1. Günlük Hayat Analojisi: Okul Kütüphanesi**
Diyelim ki kütüphanede **1.000.000** kitap var ve ben sana "Nutuk" kitabını bulmanı söylüyorum.
• **Dizi Mantığı (Brute Force):** En baştaki raftan başlarsın, her kitaba tek tek bakarsın. Kitap en sondaysa 1 milyon işlem yaparsın. (Hız: $O(n)$)
• **Sıralama Mantığı (Sorting):** Önce tüm kitapları alfabetik dizersin (bu çok vakit alır), sonra ortadan açıp "N" harfini bulursun. (Hız: $O(n \log n)$)
• **Hash Mantığı:** Kütüphanenin girişinde bir makine var. Kitabın adını yazıyorsun, makine sana anında **"3. Kat, 5. Raf, 12. Sıra"** diyor. Gidip şak diye alıyorsun. (Hız: $O(1)$ - Yani sabit zaman)

---

### **2. "Hash" Nedir? (Sihirli Kutu)**

Hash aslında bir **fonksiyon (matematiksel kutu)**dur. Bu kutunun içine ne atarsan at (bir sayı, bir isim, koca bir metin), kutu sana o girdiye özel bir **adres (sayı)** üretir.

1. **Girdi:** "elma" -> **Kutu (Hash Function)** -> **Çıktı:** 5 numaralı adres.
2. **Girdi:** "armut" -> **Kutu (Hash Function)** -> **Çıktı:** 12 numaralı adres.

Bilgisayar, "elma"nın 5 numaralı adreste olduğunu bildiği için, sen ona "elma var mı?" dediğinde listeyi taramaz. Hemen 5 numaralı adrese bakar; orası doluysa "Evet, var" der.

### **4. Hash Neden Çok Hızlı?**

Sıralama (sorting) yaparken sayıları birbirleriyle **kıyaslamak** zorundasın (bu mu büyük, şu mu?). Hash mantığında kıyaslama yoktur. Her verinin "adresi" bellidir.

> Siber Güvenlik Notu: Siber güvenlikte kullandığın MD5 veya SHA-256 da birer hash fonksiyonudur. Bir dosyanın hash'ini alırsın, dosya 1 GB olsa bile sana 64 karakterlik bir kod verir. Dosyada tek bir virgül değişse, o adres (hash kodu) tamamen değişir. LeetCode'da kullandığımız Hash Map'ler de bu mantığın çok daha basit ve hızlı versiyonlarıdır
> 

---

### **3. Çözdüğümüz Sorularda Ne İşimize Yaradı?**

### **Contains Duplicate (Eleman Tekrarı) Örneği:**

Bir `set()` (küme) oluşturduğunda aslında bir Hash tablosu açarsın.

- `[1, 2, 3, 1]` listesinde gezerken:
    1. `1` geldi: "1 numara boş mu?" Evet. Oraya bir işaret koy.
    2. `2` geldi: "2 numara boş mu?" Evet. Oraya işaret koy.
    3. `3` geldi: "3 numara boş mu?" Evet. Oraya işaret koy.
    4. `1` geldi: "1 numara boş mu?" **Hayır, dolu!** -> Demek ki bu elemanı daha önce gördüm. Hemen `True` dön.

Hiçbir şeyi birbirliyle kıyaslamadık, sadece "Adres dolu mu?" diye baktık.

### **Valid Anagram (Harf Sayma) Örneği:**

Burada bir sözlük (`dict`) kullandık. Sözlükler de Hash mantığıyla çalışır.

- `"anagram"` kelimesinde:
    - `a` harfi -> `a` adresindeki sayacı 1 artır.
    - `n` harfi -> `n` adresindeki sayacı 1 artır.
- Bilgisayar `a` harfinin yerini (adresini) bildiği için, tüm sözlüğü tarayıp `a` nerede diye bakmaz. Direkt gidip sayıyı günceller.

---

### **4. Neden Çok Hızlı?**

Sıralama (Sorting) yaptığımızda bilgisayar elemanları yer değiştirmek için birbiriyle kıyaslar: "10, 5'ten büyük mü? Evet, yer değiştir." Bu kıyaslamalar vakit alır.

Hash mantığında ise **kıyaslama yoktur, adrese gitme vardır.**

### **5. Özet: Mühendis Gibi Düşün**

- **Arama yapman gerekiyorsa** (Bu eleman burada var mı?): **Set** (Hash) kullan.
- **Bir şeye karşılık bir değer tutman gerekiyorsa** (Bu harften kaç tane var?): **Map/Dictionary** (Hash) kullan.

### **5. Özet: Ne Zaman Hash Kullanmalıyım?**

- Eğer bir şeyin **var olup olmadığını** kontrol edeceksen (`set`).
- Eğer bir şeyin **kaç tane olduğunu (frekansını)** sayacaksan (`dict` / Hash Map).
- Eğer bir veriye bir **anahtar (key)** ile anında ulaşmak istiyorsan.