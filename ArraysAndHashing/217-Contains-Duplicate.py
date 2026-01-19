"""
PROBLEM: 217. Contains Duplicate
PLATFORM: LeetCode
DIFFICULTY: Easy
LINK: https://leetcode.com/problems/contains-duplicate/

=================================================

1. PROBLEMİN TANIMI
   Bir tam sayı dizisi (nums) veriliyor. Eğer dizide herhangi bir değer en az iki kez geçiyorsa True,
   her eleman benzersizse False döndürülmelidir.

2. ÇÖZÜM YAKLAŞIMLARI (A, B, C)
   
   A) KABA KUVVET (BRUTE FORCE)
   ----------------------------
   - Mantık: İç içe iki döngü kurup her elemanı diğer tüm elemanlarla kıyaslamak.
   - Zaman Karmaşıklığı: O(n^2) -> Liste büyüdükçe performans felaketleşir.
   - Sektör Görüşü: Mülakatlarda bu çözümü sadece "en kötü ihtimali biliyorum" demek için anlat, 
     ama asla kodlama. Sistem kilitlenmesine neden olabilir.
   
   B) SIRALAMA (SORTING)
   ---------------------
   - Mantık: Önce diziyi sırala, sonra yan yana duran elemanları kontrol et.
   - Zaman Karmaşıklığı: O(n log n) (Sıralama maliyeti).
   - Alan Karmaşıklığı: O(1) veya O(n) (Algoritmaya göre).
   - Neden Seçilir?: Eğer bellek (RAM) kısıtlıysa (Gömülü sistemler) tercih edilebilir.

   C) HASH SET (KÜME KULLANIMI) - [SEÇİLEN OPTİMAL ÇÖZÜM]
   ------------------------------------------------------
   - Mantık: Bir "ziyaret edilenler" listesi (Set) tut. "Ben bunu daha önce gördüm mü?" diye sor.
   - Zaman Karmaşıklığı: O(n) -> Diziyi sadece bir kez tarar.
   - Alan Karmaşıklığı: O(n) -> En kötü ihtimalle tüm elemanları bellekte tutar.
   - Neden En Uygun?: Modern backend sistemlerinde CPU time, RAM'den daha değerlidir.
"""

from typing import List

class Solution:
    # ---------------------------------------------------------
    # A) KABA KUVVET (BRUTE FORCE)
    # Zaman: O(n^2) | Alan: O(1)
    # NOT: Bu yöntem büyük verilerde Time Limit Exceeded (TLE) hatası verir.
    # ---------------------------------------------------------
    def containsDuplicate_BruteForce(self, nums: List[int]) -> bool:
        n = len(nums)
        # İlk döngü ile her bir elemanı sırayla seçiyoruz
        for i in range(n):
            # İkinci döngü ile seçilen elemanı kendinden sonrakilerle kıyaslıyoruz
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True  # Eşleşme bulundu
        return False  # Hiçbir eşleşme bulunamadı

    # ---------------------------------------------------------
    # B) SIRALAMA (SORTING) - SENİN ÇÖZÜMÜN
    # Zaman: O(n log n) | Alan: O(1) veya O(n)
    # NOT: Veriyi değiştirir (sıralar) ama ekstra hafıza kullanmaz.
    # ---------------------------------------------------------
    def containsDuplicate_Sorting(self, nums: List[int]) -> bool:
        # 1. Diziyi küçükten büyüğe sırala (O(n log n) maliyet)
        nums.sort()

        # 2. Sadece yan yana olan elemanlara bak (Tek bir döngü)
        # len(nums) - 1 yapıyoruz çünkü i+1'e bakarken dışarı taşmamalıyız
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True # Yan yana aynı sayı varsa tekrar vardır
                
        return False

    # ---------------------------------------------------------
    # C) HASH SET (KÜME KULLANIMI) - EN OPTİMAL (LEETCODE İÇİN BUNU KULLAN)
    # Zaman: O(n) | Alan: O(n)
    # ---------------------------------------------------------
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Boş bir küme (set) oluştur. Kümede arama yapmak O(1) yani anlıktır.
        seen = set()

        for num in nums:
            # Eğer sayı daha önce kümeye eklenmişse, bu bir tekrardır
            if num in seen:
                return True
            # Sayıyı daha önce görmediysek kümemize ekliyoruz
            seen.add(num)
            
        return False