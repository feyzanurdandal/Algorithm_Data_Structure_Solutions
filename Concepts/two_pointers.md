# 📝 CONCEPTS: Two Pointers (İki İşaretçi) Stratejisi

### **1. Gerçek Hayat Analojisi: Halı Katlama ve Arama Ekibi**

> **Senaryo:** Çok uzun bir halınız var ve halının iki ucunda birer leke olup olmadığını kontrol etmeniz gerekiyor.

* **Dizi Mantığı (Verimsiz):** Halının en başından başlarsın, en sonuna kadar gidersin. Sonra tekrar en sona gidip en başa kadar bakarsın. Çok fazla yol yürürsün. Bu, enerjini (ve işlemciyi) boşa harcamaktır.
* **Two Pointers Mantığı (Zekice):** İki kişi olduğunuzu düşünün. Biriniz halının **en solunda (L)**, diğeriniz **en sağında (R)** durur. Aynı anda merkeze doğru yürümeye başlarsınız ve her adımda birbirinize *"Sende bir şey var mı?"* diye sorarsınız. Halının ortasında buluştuğunuzda tüm halıyı kontrol etmiş olursunuz ama her noktadan sadece **bir kez** geçilmiştir.

---

### **2. "Two Pointers" Nedir? (Yürüyüş Stratejisi)**

Bu yöntemde iki tane değişken (indeks) tutarız. Genellikle `L` (Left) ve `R` (Right) olarak adlandırılırlar. Bu işaretçiler dizinin içinde belirli kurallara göre hareket ederler.



| Tür | Açıklama | Örnek |
| :--- | :--- | :--- |
| **Zıt Yönlerden Merkeze (Converging)** | İşaretçiler iki uçtan başlar ve ortada buluşana kadar birbirlerine yaklaşırlar. | `Valid Palindrome`, `Two Sum II` |
| **Aynı Yönde (Fast & Slow)** | İki işaretçi de baştan başlar ama biri diğerinden daha hızlı/farklı kuralla ilerler. | `Linked List Cycle`, `Remove Duplicates` |

---

### **3. Neden Çok Hızlı? ($O(n)$ Gücü)**

Normalde "İç içe döngü" kullanarak yapılan işlemler $O(n^2)$ sürer. Bu, liste 10 kat büyüdüğünde işlemin 100 kat yavaşlaması demektir. Two Pointers kullandığımızda ise dizideki her elemana en fazla bir kez bakılır.

> **💡 Mühendislik Notu:** $O(n^2)$ süren bir işlemi $O(n)$ süresine indirmek, bir yazılımın saniyeler içinde değil, milisaniyeler içinde çalışmasını sağlar. Bu, milyonlarca kullanıcısı olan bir sistemde (veya mülakatlarda) hayati önemdedir.

---

### **4. Çözdüğümüz Sorularda Ne İşimize Yaradı?**

**Valid Palindrome Örneği:**
* **L:** En baştaki harfe bakar.
* **R:** En sondaki harfe bakar.
* **İşlem:** "Harfler aynı mı?" Evetse, ikisi de birer adım merkeze yaklaşır. Eğer farklıysa, anında `"False"` döneriz. Tüm yolu yürümemize gerek kalmaz; hatayı bulduğumuz an işi bitiririz (**Early Return**).



---

### **5. Özet: Ne Zaman Two Pointers Kullanmalıyım?**

Mülakatta şu üç işareti görürsen aklına hemen Two Pointers gelmeli:
1.  **Sıralı (Sorted)** bir dizi verildiyse ve bir şey araman isteniyorsa.
2.  Dizinin **simetrisini** kontrol etmen gerekiyorsa (Palindrom gibi).
3.  Bir diziyi **"yerinde" (in-place)**, yani ekstra hafıza harcamadan düzenlemen isteniyorsa.

---

### **6. Trade-offs (Ödünleşimler)**

* **Avantajı:** **Bellek dostudur!** ($O(1)$ Space Complexity). Yeni bir dizi veya Hash Map oluşturman gerekmez, sadece iki sayı (indeks) tutarsın.
* **Dezavantajı:** Verinin genellikle **sıralı (sorted)** olması gerekir. Eğer veri karışık ise Two Pointers kullanmak için önce sıralama yapman gerekir ($O(n \log n)$), bu da başlangıçta vakit alabilir.