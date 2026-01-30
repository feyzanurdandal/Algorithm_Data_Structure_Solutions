"""
PROBLEM: 347. Top K Frequent Elements
PLATFORM: LeetCode
DIFFICULTY: Medium
LINK: https://leetcode.com/problems/top-k-frequent-elements/

=================================================

1. PROBLEMİN TANIMI
   Verilen bir tam sayı dizisinde (nums) en çok tekrar eden (frekansı en yüksek olan) 
   ilk 'k' elemanı bulun ve döndürün.

2. ÇÖZÜM YAKLAŞIMLARI (A, B, C)
   
   A) HASH MAP + SIRALAMA (SORTING)
   -------------------------------
   - Mantık: Önce her sayının kaç kez geçtiğini bir sözlükte (Hash Map) say. 
     Ardından bu sözlüğü "tekrar sayılarına" göre büyükten küçüğe sırala.
   - Zaman Karmaşıklığı: O(n log n) -> Sıralama maliyetinden dolayı.
   - Sektör Görüşü: Yazması en kolay yöntemdir, küçük verilerde tercih edilir.

   B) HASH MAP + HEAP (YIĞIN)
   --------------------------
   - Mantık: Sayıları saydıktan sonra bir "Min-Heap" yapısı kullanarak k boyutu 
     kadar en büyük elemanları koru.
   - Zaman Karmaşıklığı: O(n log k) -> Sıralamadan daha hızlıdır.

   C) KOVA SIRALAMASI (BUCKET SORT) - [SEÇİLEN OPTİMAL ÇÖZÜM]
   --------------------------------------------------------
   - Mantık: Frekansları (tekrar sayılarını) bir listenin indeksi (çekmece no) olarak kullan. 
     Örneğin, 5 kez geçen her şeyi 5. çekmeceye koy. Sondan başla, k tane topla.
   - Zaman Karmaşıklığı: O(n) -> Diziyi sadece birkaç kez tarar, hiç sıralama yapmaz.
   - Neden En Uygun?: En yüksek performansı verir, "Senior" seviye bir çözümdür.
"""

from typing import List
from collections import Counter

class Solution:
    # ---------------------------------------------------------
    # A) HASH MAP + SIRALAMA (BASİT VE ANLAŞILIR)
    # Zaman: O(n log n) | Alan: O(n)
    # ---------------------------------------------------------
    def topKFrequent_Sorting(self, nums: List[int], k: int) -> List[int]:
        # 1. Sayıları say: {1: 3, 2: 2, 3: 1}
        count = Counter(nums)
        
        # 2. Sözlükteki anahtarları (sayıları), değerlerine (frekans) göre sırala
        # sorted() fonksiyonu burada frekansı yüksek olanı öne alır
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # 3. İlk k tanesini döndür
        return sorted_elements[:k]

    # ---------------------------------------------------------
    # C) KOVA SIRALAMASI (BUCKET SORT) - EN OPTİMAL
    # Zaman: O(n) | Alan: O(n)
    # ---------------------------------------------------------
    def topKFrequent(self, nums, k):
        # --- 1. ADIM: SAYILARI SAYMA (FREKANS TABLOSU) ---
        # Burada bir 'dictionary' (sözlük) kullanıyoruz. 
        # Amacımız: {sayı: kaç_kere_geçti} bilgisini tutmak.
        count = {} 
        
        for n in nums:
            # count.get(n, 0) şu demek: 
            # "Sözlükte 'n' sayısına bak. Varsa değerini getir, yoksa 0 kabul et."
            # Üzerine 1 ekleyerek sayacı güncelliyoruz.
            count[n] = 1 + count.get(n, 0)

        # --- 2. ADIM: KOVALARI OLUŞTURMA (BUCKET SORT) ---
        # freq, iç içe listelerden oluşan dev bir listedir.
        # Neden len(nums) + 1? Çünkü bir sayı en fazla listenin tamamı kadar (n tane) tekrar edebilir.
        # Görünümü şuna benzer: [[], [], [], [], ...] (Hepsi boş kutular)
        freq = [[] for i in range(len(nums) + 1)]
        
        # count.items() bize sözlükteki (sayı, tekrar_adedi) çiftlerini verir.
        for n, c in count.items():
            # 'c' (tekrar adedi) bizim indeksimiz oluyor.
            # Örneğin; 1 sayısı 3 kere geçtiyse, onu 3. indeksteki kutuya atıyoruz.
            freq[c].append(n)

        # --- 3. ADIM: EN ÇOK TEKRAR EDENLERİ TOPLAMA ---
        # En popülerleri saklayacağımız boş bir liste
        res = []
        
        # range(başlangıç, bitiş, adım)
        # Listenin sonundan (len(freq) - 1) başlıyoruz, 0'a kadar, geriye doğru (-1) gidiyoruz.
        # Çünkü en yüksek frekanslar (en çok tekrar edenler) listenin sonundadır.
        for i in range(len(freq) - 1, 0, -1):
            # i. indeksteki kutunun (listenin) içindeki sayıları tek tek alıyoruz
            for n in freq[i]:
                res.append(n)
                # Eğer istediğimiz sayıya (k) ulaştıysak, hemen sonucu döndür ve bitir.
                if len(res) == k:
                    return res

# =================================================
# SENIOR MÜHENDİS NOTLARI:
# 1. Neden Bucket Sort?: Normalde sıralama O(n log n) sürer. Ancak burada 
#    "maksimum frekansın" dizi boyutuyla (n) sınırlı olduğunu bildiğimiz için 
#    frekansları doğrudan indeks (adres) olarak kullanarak O(n) hıza ulaştık.
# 2. Python Pratiği: count.get(n, 0) yöntemi, Python'da "KeyError" almadan 
#    sözlüğe veri eklemenin en güvenli ve temiz yoludur.
# 3. Mülakat İpucu: Bu soruda "Herhangi bir sırada dönebilirsiniz" (any order) 
#    denmesi, Bucket Sort veya Heap gibi sıralamayı tam yapmayan ama 
#    sonucu doğru veren hızlı yöntemlerin önünü açar.
# =================================================

"""
Bucket Sort nasıl çalışıyor?
Olay şu: Dizinin uzunluğu kadar çekmecen olduğunu hayal et.
Eğer "5" sayısı 3 kere geçtiyse, onu gidip 3 numaralı çekmeceye fırlatıyorsun.
Eğer "10" sayısı da 3 kere geçtiyse, o da 3 numaralı çekmeceye gidiyor.
Sonra en büyük numaralı çekmeceden (yani en çok tekrar edenden) başlayarak çekmeceleri boşaltıyorsun.
Maliyet: $O(n)$ (Çünkü hiç sıralama yapmadın, sadece çekmecelere koyup aldın).
"""