# --- NOTES6.PY: İLERİ SEVİYE FONKSİYONLAR & KISAYOLLAR ---
# Bu dosya, standart fonksiyonların ötesine geçen, kodu kısaltan
# ve daha esnek hale getiren yapıları içerir.

### 1. **KWARGS (Key-Word Arguments) - Esnek Parametreler
# Fonksiyona kaç tane isimlendirilmiş parametre geleceğini bilmiyorsan kullanılır.
# Gelen veriyi bir SÖZLÜK (Dictionary) olarak tutar.

def kisi_bilgileri(**kwargs):
    """İstenildiği kadar 'anahtar=değer' bilgisini kabul eder."""
    print(f"Gelen Veri Tipi: {type(kwargs)}") # <class 'dict'>
    
    for anahtar, deger in kwargs.items():
        print(f"{anahtar}: {deger}")

# Kullanımı:
# kisi_bilgileri(ad="Ahmet", yas=25, sehir="Mersin", meslek="Mühendis")
# kisi_bilgileri(marka="BMW", model=2023) # İstediğin kadar ekle


### 2. LAMBDA (Anonim/Tek Satırlık Fonksiyonlar)
# Sadece tek bir işlem yapan küçük fonksiyonlar için `def` yazmak yerine kullanılır.
# Yapı: lambda girisler : yapilacak_islem

# Normal Fonksiyon:
def kare_al_normal(x):
    return x ** 2

# Lambda Hali:
kare_al_lambda = lambda x: x ** 2

# Kullanımı:
# print(kare_al_lambda(5)) # Çıktı: 25
# print((lambda x, y: x + y)(3, 5)) # Direkt kullanım, Çıktı: 8


### 3. RECURSIVE (Özyinelemeli) FONKSİYONLAR
# Bir fonksiyonun, görevi bitirmek için KENDİNİ TEKRAR ÇAĞIRMASIDIR.
# Genellikle Matematiksel işlemlerde (Faktöriyel gibi) kullanılır.
# DİKKAT: Durma noktası (Base Case) olmazsa sonsuz döngüye girer!

def faktoriyel(n):
    # 1. Durma Noktası (Base Case)
    if n == 1:
        return 1
    
    # 2. Kendini Çağırma (Recursive Step)
    # 4! = 4 * 3! -> 3! = 3 * 2! ...
    return n * faktoriyel(n - 1)

# print(faktoriyel(4)) # Çıktı: 24 (4*3*2*1)


### 4. FONKSİYON İÇİNDE FONKSİYON (Higher Order Functions)
# Bir fonksiyon, başka bir fonksiyonu parametre olarak alabilir.

def islem_yap(fonksiyon, sayi):
    """Verilen sayıyı, verilen fonksiyona sokar."""
    return fonksiyon(sayi)

kup_al = lambda x: x**3

# print(islem_yap(kup_al, 3)) # Çıktı: 27


### 5. LIST COMPREHENSION vs FOR DÖNGÜSÜ (Filtreleme)
# Bir listeden belli şartı sağlayanları seçmek için iki yöntem.

kelimeler = ["karpuz", "elma", "armut", "kardan adam", "kayak", "kar yağışı"]

# YÖNTEM A: Klasik For Döngüsü (Uzun Yol)
def kar_filtrele_uzun(liste):
    sonuc = []
    for kelime in liste:
        if "kar" in kelime:
            sonuc.append(kelime)
    return sonuc

# YÖNTEM B: List Comprehension (Profesyonel Kısa Yol)
# Yapı: [eleman FOR eleman IN liste IF kosul]
def kar_filtrele_kisa(liste):
    return [kelime for kelime in liste if "kar" in kelime]

# print(kar_filtrele_kisa(kelimeler)) 
# Çıktı: ['karpuz', 'kardan adam', 'kar yağışı']