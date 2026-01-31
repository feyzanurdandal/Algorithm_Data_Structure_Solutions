"""
PROBLEM: 125. Valid Palindrome
PLATFORM: LeetCode
DIFFICULTY: Easy
LINK: https://leetcode.com/problems/valid-palindrome/

=================================================

1. PROBLEMİN TANIMI
   Bir string (s) veriliyor. Tüm büyük harfleri küçüğe çevirdikten ve tüm alfanümerik 
   (harf ve rakam) olmayan karakterleri temizledikten sonra, stringin önden ve arkadan 
   okunuşunun aynı (palindrom) olup olmadığını kontrol etmemiz gerekir.

2. ÇÖZÜM YAKLAŞIMLARI (A, B)
   
   A) PYTHONIC ÇÖZÜM (TEMİZLE VE TERS ÇEVİR)
   ----------------------------
   - Mantık: Stringi bir döngüyle gezip sadece harf ve rakamları al, hepsini küçült. 
     Ardından oluşan yeni stringi Python'ın dilimleme (slicing) özelliğiyle ters çevirip kıyasla.
   - Zaman Karmaşıklığı: O(n) -> Stringi baştan sona tararız.
   - Alan Karmaşıklığı: O(n) -> Temizlenmiş stringi ve tersini hafızada tutmak için ek yer gerekir.
   - Sektör Görüşü: Kodun kısalığı ve okunabilirliği açısından harikadır. "Yazılımcı dostu" bir çözümdür.
   
   B) İKİ İŞARETÇİ (TWO POINTERS) - [OPTIMAL ÇÖZÜM]
   ---------------------
   - Mantık: Stringin başına ve sonuna iki işaretçi (L ve R) koy. Geçersiz karakterleri atlayarak 
     merkeze doğru ilerle ve karakterleri karşılıklı kıyasla.
   - Zaman Karmaşıklığı: O(n) -> Stringi en fazla bir kez tararız.
   - Alan Karmaşıklığı: O(1) -> Ekstra bir string oluşturmayız, sadece iki adet değişken tutarız.
   - Neden En Uygun?: Bellek kullanımı (RAM) açısından en verimli yöntemdir. Mülakatlarda 
     genelde bu "in-place" (yerinde) çözüm beklenir.
"""

class Solution:
    # ---------------------------------------------------------
    # A) PYTHONIC ÇÖZÜM (SENİN KURDUĞUN MANTIK)
    # Zaman: O(n) | Alan: O(n)
    # ---------------------------------------------------------
    def isPalindrome_Pythonic(self, s: str) -> bool:
        # 1. Aşama: Temizlik ve Küçültme
        # 'char.isalnum()' -> karakter harf veya sayı mı?
        # 'char.lower()' -> karakteri küçük harfe çevir
        new_s = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Aşama: Ters Çevirme ve Kıyaslama
        # [::-1] Python'da bir stringi ters çevirmenin en hızlı yoludur
        return new_s == new_s[::-1]

    # ---------------------------------------------------------
    # B) İKİ İŞARETÇİ (TWO POINTERS) - BELLEK DOSTU
    # Zaman: O(n) | Alan: O(1)
    # ---------------------------------------------------------
    def isPalindrome(self, s: str) -> bool:
        # Başlangıç ve bitiş indekslerini belirliyoruz
        l, r = 0, len(s) - 1
        
        # İşaretçiler ortada buluşana kadar devam et
        while l < r:
            # Sol işaretçiyi geçerli bir karakter bulana kadar sağa kaydır
            # 'while l < r' kontrolü indeks dışına taşmamak için kritiktir
            while l < r and not s[l].isalnum():
                l += 1
            
            # Sağ işaretçiyi geçerli bir karakter bulana kadar sola kaydır
            while r > l and not s[r].isalnum():
                r -= 1
            
            # Karakterleri küçülterek kıyasla
            if s[l].lower() != s[r].lower():
                return False # Eşleşme yoksa palindrom değildir
            
            # Karakterler aynıysa işaretçileri merkeze doğru birer adım ilerlet
            l += 1
            r -= 1
            
        return True # Tüm kontrolleri geçtiyse palindromdur