"""PROBLEM: 1. Two Sum
PLATFORM: LeetCode
DIFFICULTY: Easy
LINK: https://leetcode.com/problems/two-sum/

=================================================

1. PROBLEMİN TANIMI
   Bir tam sayı dizisi (nums) ve bir hedef değer (target) veriliyor. Toplamları 
   hedefe eşit olan iki sayının İNDEKSLERİNİ döndürmemiz gerekiyor.
   Kural: Aynı elemanı iki kez kullanamazsın ve her zaman tek bir çözüm vardır.

2. ÇÖZÜM YAKLAŞIMLARI (A, B)
   
   A) KABA KUVVET (BRUTE FORCE)
   ----------------------------
   - Mantık: İç içe iki döngü kur. Her sayıyı, kendinden sonra gelen tüm sayılarla 
     topla ve hedefi bulup bulmadığına bak.
   - Zaman Karmaşıklığı: O(n^2) -> Liste 10.000 elemanlıysa 100 milyon işlem demektir.
   - Sektör Görüşü: Kabul edilemez derecede yavaştır. Sadece mantığı kurmak için başlangıçtır.

   B) HASH MAP (SÖZLÜK KULLANIMI) - [SEÇİLEN OPTİMAL ÇÖZÜM]
   ------------------------------------------------------
   - Mantık: Diziyi bir kez gezerken "Deftere" (Hash Map) bak: "Hedefe ulaşmam için 
     gereken sayı daha önce geçti mi?"
   - Zaman Karmaşıklığı: O(n) -> Diziyi sadece tek bir sefer baştan sona tarar.
   - Alan Karmaşıklığı: O(n) -> Sayıları ve yerlerini hafızada tutmak için yer harcar.
   - Neden En Uygun?: Hız saniyelerden milisaniyelere iner. "Gördüğünü unutma" prensibiyle çalışır."""

from typing import List

class Solution:
    # ---------------------------------------------------------
    # A) KABA KUVVET (BRUTE FORCE)
    # Zaman: O(n^2) | Alan: O(1)
    # ---------------------------------------------------------
    def twoSum_BruteForce(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # ---------------------------------------------------------
    # B) HASH MAP (SÖZLÜK) - EN OPTİMAL
    # Zaman: O(n) | Alan: O(n)
    # ---------------------------------------------------------
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 'gorulenler' sözlüğü: { Sayı Değeri : İndeks } şeklinde tutacak
        gorulenler = {}

        # Dizide hem indeksi hem de sayıyı alarak geziyoruz
        for i, num in enumerate(nums):
            # Hedefe ulaşmak için ihtiyacımız olan "tamamlayıcı" sayı
            diff = target - num
            
            # Bu sayı daha önce defterimize (hash map) kaydedilmiş mi?
            # NOT: Sözlükte 'in' sorgusu yapmak O(1) hızındadır (Sihirli Kutu!)
            if diff in gorulenler:
                # Varsa: O sayının indeksi ile şu anki indeksi döndür
                return [gorulenler[diff], i]
            
            # Yoksa: Şu anki sayıyı ve yerini deftere kaydet, ilerle
            gorulenler[num] = i
            
        return []

# =================================================
# SENIOR MÜHENDİS NOTLARI:
# 1. Neden Hash Map?: 'num2 in nums' (liste) O(n) iken, 
#    'diff in gorulenler' (sözlük/hash) O(1) sürededir. 
#    Döngü içinde döngü kurmaktan bizi kurtarır.
# 2. Tek Geçiş (One-pass): Sayıları önce deftere yazıp sonra bakmak yerine, 
#    gezerken bakıp sonra yazıyoruz. Bu sayede aynı sayıyı iki kez 
#    kullanma riskini (örn: target=6, sayı=3) otomatik eliyoruz.
# 3. Mülakat İpucu: Mülakatçıya "Dizi sıralı mı?" diye sor. 
#    Eğer sıralıysa "Two Pointers" (İki İşaretçi) yöntemi daha az RAM harcar.
# =================================================