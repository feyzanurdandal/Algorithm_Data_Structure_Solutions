"""
PROBLEM: 242. Valid Anagram
PLATFORM: LeetCode
DIFFICULTY: Easy
LINK: https://leetcode.com/problems/valid-anagram/

==============================================================

1. PROBLEMİN TANIMI
   Verilen iki string'in (s ve t) birbirinin anagramı olup olmadığını belirlemek. 
   Temel kural: Her iki kelime de aynı harfleri, aynı miktarda içermelidir.

2. ÇÖZÜM YAKLAŞIMLARI (A, B, C)

   A) SIRALAMA (SORTING)
   ---------------------
   - Mantık: Kelimeleri alfabetik sıraya diz. Eşitlerse anagramdır.
   - Zaman Karmaşıklığı: O(n log n) -> Sıralama maliyeti.
   - Alan Karmaşıklığı: O(n) -> Python'da stringler immutable olduğu için yeni liste oluşur.
   - Kullanım: Kodun okunabilirliği öncelikliyse ve performans (hız) ikinci plandaysa.

   B) HASH MAP (DICTIONARY) - [SEÇİLEN OPTİMAL YÖNTEM]
   ---------------------------------------------------
   - Mantık: Harf frekanslarını (sıklığını) sayan bir çizelge tut.
   - Zaman Karmaşıklığı: O(n) -> Veriyi sadece bir kez okur.
   - Alan Karmaşıklığı: O(k) -> k = Alfabedeki harf sayısı (İngilizce için 26).
   - Kullanım: Standart mülakat çözümü ve yüksek performans gerektiren backend sistemleri.

   C) PYTHONIC KISA YOL (COUNTER)
   ------------------------------
   - Mantık: Python'un `collections.Counter` sınıfını kullanarak otomatik sayım yapmak.
   - Sektör Görüşü: Günlük hayatta en çok kullanılan pratik yöntem.

3. SEKTÖR UYGULAMALARI VE İPUÇLARI
   - Unicode vs ASCII: "Input sadece İngilizce mi yoksa Emoji/Çince içeriyor mu?" sorusu kritiktir.
     Sadece İngilizce ise 26'lık bir Array, Unicode ise Hash Map kullanılır.
   - Siber Güvenlik (Frekans Analizi): Bu algoritma, Kriptografideki "Frequency Analysis" 
     saldırısının temelidir. Şifreli metindeki harf dağılımını, bilinen dille kıyaslayarak
     şifreyi kırmak için bu Hash Map mantığı kullanılır.

4. TEKNİK KAZANIMLAR
   - Edge Case: `len(s) != len(t)` kontrolü ile gereksiz işlemden kaçınma.
   - Time-Space Trade-off: Hız için bellekten (Hash Map), bellek için hızdan (Sorting) vazgeçme dengesi.
"""

from collections import Counter

class Solution:
    # ---------------------------------------------------------
    # A) SIRALAMA (SORTING) YAKLAŞIMI
    # Zaman: O(n log n) | Alan: O(n)
    # ---------------------------------------------------------
    def isAnagram_Sorting(self, s: str, t: str) -> bool:
        # 1. Uzunluklar eşit değilse anagram olamazlar (Hızlı elenme/Edge Case)
        if len(s) != len(t):
            return False

        # 2. Stringleri harf sırasına diz ve karşılaştır
        return sorted(s) == sorted(t)

    # ---------------------------------------------------------
    # B) HASH MAP (DICTIONARY) - EN OPTİMAL MÜLAKAT ÇÖZÜMÜ
    # Zaman: O(n) | Alan: O(1) (Alfabe sınırı sabit olduğu için)
    # ---------------------------------------------------------
    def isAnagram_HashMap(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}
        
        # Tek bir döngüde her iki string'in harflerini sayıyoruz
        for i in range(len(s)):
            # get(harf, 0) -> harf varsa sayısını getir, yoksa 0 getir
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # İki sözlük birbiriyle aynı mı?
        return countS == countT

    # ---------------------------------------------------------
    # C) PYTHONIC KISA YOL (COUNTER) - SEKTÖR STANDARDI
    # Zaman: O(n) | Alan: O(1)
    # ---------------------------------------------------------
    def isAnagram(self, s: str, t: str) -> bool:
        """
        LeetCode'a gönderilecek asıl çözüm (Pythonic Way).
        Counter, arka planda Hash Map mantığını kullanır.
        """
        return Counter(s) == Counter(t)