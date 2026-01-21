"""PROBLEM: 49. Group Anagrams
PLATFORM: LeetCode
DIFFICULTY: Medium
LINK: https://leetcode.com/problems/group-anagrams/

=================================================

1. PROBLEMİN TANIMI
   Verilen bir kelime listesinde (strs) birbirinin anagramı olanları (aynı harfleri 
   aynı sayıda içerenler) gruplayarak bir liste içinde döndürün.

2. ÇÖZÜM YAKLAŞIMLARI (A, B)
   
   A) SIRALAMA (SORTING) & HASH MAP
   -------------------------------
   - Mantık: Her kelimenin harflerini alfabetik sırala. Sıralanmış hali "ortak anahtar" 
     (key) yap. Aynı anahtara sahip kelimeleri bir grupta topla.
   - Zaman Karmaşıklığı: O(n * k log k) -> n: kelime sayısı, k: kelime uzunluğu.
   - Neden Seçilir?: Kodun okunabilirliği en yüksektir, anlaşılması kolaydır.

   B) KARAKTER SAYMA (COUNTING) - [EN OPTİMAL ÇÖZÜM]
   ------------------------------------------------
   - Mantık: Sıralama yapmak yerine her kelime için 26 harflik bir frekans dizisi 
     oluştur. Bu diziyi anahtar (key) yaparak kelimeleri grupla.
   - Zaman Karmaşıklığı: O(n * k) -> Sıralama maliyetinden kurtulduğumuz için en hızlıdır.
   - Neden Seçilir?: Kelime uzunluklarının (k) çok büyük olduğu durumlarda performans sağlar."""

from collections import defaultdict

class Solution:
    # ---------------------------------------------------------
    # A) SIRALAMA (SORTING) YAKLAŞIMI
    # Zaman: O(n * k log k) | Alan: O(n * k)
    # ---------------------------------------------------------
    def groupAnagrams_Sorting(self, strs: list[str]) -> list[list[str]]:
        # Defaultdict: Anahtar yoksa otomatik boş liste [] oluşturur
        res = defaultdict(list)

        for s in strs:
            # sorted(s) listesini "".join() ile string'e çevirip anahtar yapıyoruz
            # Çünkü Python'da listeler sözlük anahtarı olamaz (unhashable)
            key = "".join(sorted(s))
            #Orijinal kelimeyi bu sayı kombinasyonuna sahip gruba ekle
            res[key].append(s)

        return list(res.values())

    # ---------------------------------------------------------
    # B) KARAKTER SAYMA (COUNTING) YAKLAŞIMI - EN OPTİMAL
    # Zaman: O(n * k) | Alan: O(n * k)
    # ---------------------------------------------------------
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res = defaultdict(list)

        for s in strs:
            # 1. 26 harf için (a-z) bir sayaç listesi oluştur
            count = [0] * 26 
            
            # 2. Kelime içindeki her harfin kaç kez geçtiğini say
            for char in s:
                # ord() ile harfin ASCII değerini alıp 0-25 arasına sığdırıyoruz
                count[ord(char) - ord('a')] += 1
            
            # 3. Listeyi anahtar olarak kullanmak için 'tuple' yapıyoruz
            # Tuple değiştirilemez (immutable) olduğu için hash edilebilir.
            res[tuple(count)].append(s)

        return list(res.values())

# =================================================
# SENIOR MÜHENDİS NOTLARI:
# 1. Veri Yapısı Seçimi: defaultdict(list) kullanımı 'if key not in dict'
#    kontrolünü ortadan kaldırarak kodu daha temiz (clean code) yapar.
# 2. Hashability: Python'da sözlük anahtarı olacak objenin "değiştirilemez" 
#    olması gerekir. Bu yüzden sorted() listesini join ile string'e, 
#    count listesini ise tuple'a çevirdik.
# 3. Scalability (Ölçeklenebilirlik): Eğer kelime uzunluğu (k) milyonlarca 
#    karakter olsaydı, Sıralama yöntemi çökerdi ancak Sayma yöntemi 
#    (Counting) hala saniyeler içinde çalışırdı.
# 4. Neden İkinci Yöntem Daha Hızlı?
#    Sıralama yöntemi, kelime çok uzun olduğunda (örneğin 10.000 karakterli bir string) çok yavaşlar. 
#    Ancak Sayma yöntemi, kelime ne kadar uzun olursa olsun sadece bir kez üzerinden geçer.
# =================================================