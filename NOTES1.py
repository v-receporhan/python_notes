# --- NOTES1.PY: GİRDİ, KONTROLLER VE SAYILAR ---

### 1. Girdi Alma ve Tür Dönüşümü
# Kullanıcıdan veri almak ve bu veriyi matematiksel işlemlerde
# kullanmak için sayıya dönüştürmek gerekir.

# input(): Kullanıcıdan metin (string) veri alır.
# Örn: isim = input("Adın ne?: ")

# float(girdi): Alınan metni ondalıklı sayıya çevirir.
# Örn: not1 = float(input("1. Notu gir: ")) (Not Ortalaması)

# int(girdi): Alınan metni tam sayıya çevirir.
# Örn: how_many = int(input("Kaç zar?: ")) (Zar Atma)


### 2. Hata Yönetimi
# Kullanıcı `float` beklenen yere harf girerse programın çökmesini engeller.

# try: / except ValueError:
# Hata verebilecek kodu (genellikle `float`/`int`) dener,
# hata olursa `except` bloğu çalışır.
"""
try:
    amount_value = float(amount)
except ValueError:
    print("Geçersiz sayı")
"""
# (Proje: Döviz Çevirici)


### 3. Karar Yapıları (IF / ELIF / ELSE)
# Programın farklı durumlara göre farklı yollar izlemesini sağlar.

# if / elif / else: Koşul zinciri. Sırayla kontrol eder, doğru olanı çalıştırır.
"""
if op == '+':
    result = n1 + n2
elif op == '-':
    result = n1 - n2
else:
    result = "Geçersiz"
"""
# (Proje: Hesap Makinesi)

# 'and' (VE): Her iki koşul da doğru olmalı.
# Örn: if tam_sayi > 20 and not tam_sayi % 2 == 0:

# 'or' (VEYA): Koşullardan en az biri doğru olmalı.
# Örn: if (para >= 50 or vip_uyelik): ...


### 4. Matematik (MATH Modülü)
# import math
# from math import floor, sqrt

# math.floor(5.7): Sayıyı aşağıya (küçüğe) yuvarlar. (Çıktı: 5)
# math.sqrt(16): Sayının karekökünü alır. (Çıktı: 4.0)

# round(sayı, 1): Sayıyı en yakın değere yuvarlar (1 = virgülden sonra 1 basamak).
# Örn: ortalama_yuvarlanmis = round(ortalama, 1) (Not Ortalaması)