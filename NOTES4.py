# --- NOTES4.PY: WHILE DÖNGÜLERİ & STRING (METİN) METOTLARI ---
# Bu dosya, koşula bağlı döngüleri (while) ve metinler üzerinde
# işlem yapmayı (string metotları) öğrenmek için kullanılır.

### 1. WHILE DÖNGÜSÜ (Koşullu Döngü)
# `for` döngüsü gibi `range` veya liste uzunluğuyla sınırlı değildir;
# koşul `True` olduğu sürece çalışır. Döngü sayısının *belirsiz*
# olduğu durumlar için idealdir.

# `while kosul:`
# `kosul` doğru olduğu sürece altındaki kod bloğunu çalıştırır.
# Örn:
# sayi = 0
# while sayi < 10:
#     print(sayi)
#     sayi += 1  # (10'a kadar sayar)

# `while True:`
# Sonsuz Döngü başlatır. Durdurmak için `break` şarttır.
# Örn:
# while True:
#     secim = input("Menü (1-5): ")
#     if secim == "5":
#         break
# (Proje: Hesap Makinesi/TPS Menüsü)

# `break`
# İçinde bulunduğu döngüyü o anda durdurur ve dışarı çıkar.
# Örn:
# if sayi == -1:
#     print("Çıkılıyor...")
#     break

# `exit()`
# `break`'ten farklı olarak, döngüyü değil programın tamamını durdurur.
# Örn:
# print("Güle güle", exit())


### 2. ÖZEL DURUM KONTROLÜ (Hata Önleme)
# Projelerde, matematiksel hataları önlemek için `if` ile özel kontroller gerekir.

# Sıfıra Bölme Kontrolü:
# Bölme işlemi yapmadan önce bölen sayının 0 olup olmadığını kontrol et.
"""
elif secim == "4":
    if sayi2 == 0:
        print("Hata! Sıfıra bölünemez!")
    else:
        print(sayi1 / sayi2)
"""
# (Proje: Hesap Makinesi)

# ---

### 3. STRING (METİN) METOTLARI
# Metinler üzerinde işlem yapmak için kullanılan araçlar.

#### A. Büyük/Küçük Harf ve Temizlik

# `.capitalize()`: Metnin sadece *ilk harfini* büyük yapar.
# metin = "merhaba"
# print(metin.capitalize()) # Çıktı: "Merhaba"

# `.title()`: Metindeki *her kelimenin* ilk harfini büyük yapar.
# metin = "merhaba dünya"
# print(metin.title()) # Çıktı: "Merhaba Dünya"

# `.strip()`: Metnin *başındaki ve sonundaki* boşlukları siler.
# metin = "  boşluklu  "
# print(metin.strip()) # Çıktı: "boşluklu"

# `.lstrip()` / `.rstrip()`: Sadece *soldaki* / *sağdaki* boşlukları siler.


#### B. Bölme, Birleştirme ve Değiştirme

# `.split(ayrac)`: Metni `ayrac`'a göre böler ve LİSTE döndürür.
# metin = "merhaba,dünya"
# liste = metin.split(",") # Çıktı: ['merhaba', 'dünya']

# `ayrac.join(liste)`: Bir listenin elemanlarını `ayrac` ile birleştirip STRING yapar.
# liste = ["merhaba", "python"]
# birlesik = ",".join(liste) # Çıktı: "merhaba,python"

# `.replace("eski", "yeni")`: Metindeki "eski" değerleri "yeni" değerle değiştirir.
# metin = "python güzeldir"
# print(metin.replace("python", "java")) # Çıktı: "java güzeldir"

# `.replace("eski", "yeni", sayi)`: Sadece ilk `sayi` adet "eski" değeri değiştirir.
# metin = "python,python,python"
# print(metin.replace("python", "java", 2)) # Çıktı: "java,java,python"


#### C. Arama ve Kontrol Etme

# `.find("kelime")`: Kelimenin metin içinde başladığı *ilk index'i* verir (Bulamazsa -1 döndürür).
# metin = "python öğren"
# print(metin.find("öğren")) # Çıktı: 7

# `.count("kelime")`: Kelimenin metin içinde *kaç defa* geçtiğini sayar.
# metin = "python,python,python"
# print(metin.count("python")) # Çıktı: 3

# `.isdigit()`: String'in tamamı rakamlardan mı oluşuyor? (True/False)
# `.isalpha()`: String'in tamamı harflerden mi oluşuyor? (True/False)
# `.isalnum()`: String'in tamamı harf veya rakamlardan mı oluşuyor?
# `.islower()` / `.isupper()`: String'in tamamı küçük mü / büyük mü?


### 4. PRO SEVİYE: STRING AYRIŞTIRMA (Unpacking)
# Tek satırda hem `split`, hem `strip` hem de değişkenlere atama yapmak.

# Veri:
# metin = "104,ali,çalışkan,89"

# Yöntem:
# 1. .split(",") ile veriyi parçalara ayırır -> ["104", "ali", "çalışkan", "89"]
# 2. Her 'parca'yı .strip() ile gereksiz boşluklardan temizler.
# 3. Sonuç listesini 4 değişkene (unpacking) atar.
# numara, ad, soyad, ortalama = [parca.strip() for parca in metin.split(",")]

# Çıktı:
# print("Numara:", numara) -> Numara: 104