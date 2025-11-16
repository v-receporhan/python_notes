# --- NOTES5.PY: SET, SÖZLÜK & FONKSİYONLAR ---
# Bu dosya, Python'daki daha gelişmiş veri yapılarını (Set, Dict)
# ve kodun temel yapı taşı olan Fonksiyonları (def) içerir.

### 1. SET (Kümeler)
# Ana Özellikler: Elemanları SIRASIZDIR ve her eleman UNIQ'tir (tekrarlanmaz).
# Matematiksel küme işlemleri (birleşim, kesişim) için kullanılır.

# Set Oluşturma:
# dersler_set = {"tarih", "matematik", "fizik"}

# Set'in En Hızlı Kullanımı (Listeden Duplikatları Silme):
# number_list = [1, 2, 3, 2, 4, 5, 3]
# numbers_set = set(number_list)  # Çıktı: {1, 2, 3, 4, 5}
# number_list = list(numbers_set) # Geri listeye çevirme: [1, 2, 3, 4, 5]

# Set Metotları (Küme İşlemleri):
# .intersection(set2): İki set'in KESİŞİMİNİ (ortak elemanlar) bulur.
# .difference(set2): İlk set'in FARKINI (set2'de olmayanlar) bulur.
# .union(set2): İki set'in BİRLEŞİMİNİ (tüm elemanlar) bulur.

# Eleman Ekleme / Silme (Mutable'dır):
# dersler_set.add("kimya")
# dersler_set.remove("matematik")


### 2. DICTIONARY (Sözlükler)
# Ana Özellikler: Anahtar-Değer (Key-Value) çiftleri ile veri tutar.
# Hızlı veri arama ve gruplama için kullanılır (Okul No -> İsim gibi).

# Sözlük Oluşturma (Anahtar: Değer):
# ogrenciler_dict = {100: "ali kaya", 101: "veli ölmez"}
# ogrenciler = {101: [85, 90, 78], 102: [92, 88, 95]} # Değerler liste olabilir

# Veriye Güvenli Erişim (.get()):
# .get(key), anahtar (key) yoksa programı çökertmek yerine 'None' döndürür.
# deger = ogrenciler_dict.get(102)
# if deger is None:
#     print("Öğrenci yok.")

# Veri Ekleme / Değiştirme:
# ogrenciler_dict[100] = "fatma kaya" # Varolanı günceller veya yenisini ekler.

# Veri Silme:
# ogrenciler_dict.pop(100) # 100 key'li elemanı siler.
# del ogrenciler_dict[100] # Aynı işi yapar.

# İç İçe Veri Değiştirme (Sözlük içindeki Listeyi):
# sayilar_dict[103][1] = 40 # 103 key'li listenin 1. index'ini 40 yap.

# Sözlük Üzerinde Döngü (.items()):
# .items() kullanarak hem anahtarı hem de değeri aynı anda alırsın.
"""
for okul_no, sinav_notlari in ogrenciler.items():
    print(f"Okul No: {okul_no}")
    for notu in sinav_notlari:
        print(f"Sınav Notu: {notu}")
"""

# Tuple Listesi Üzerinde Döngü (Aynı Mantık):
# Tıpkı .items() gibi, (ad, sayfa) çiftlerini açar (Unpacking).
"""
kitaplar = [("Simyacı", 184), ("1984", 352)]
for kitap_adi, sayfa_Sayisi in kitaplar:
    if sayfa_Sayisi > 170:
        print(kitap_adi)
"""

### 3. FONKSİYONLAR (def)
# Kod tekrarını önler, kodun okunabilirliğini artırır.

# Parametre (Dışarıdan Veri Alma):
# Fonksiyonun çalışmak için ihtiyaç duyduğu veriler.
# def agirlikli_ortalama_hesapla(mt1, mt2, f):
#     # ... kodlar ...

# Return (Dışarıya Veri Döndürme):
# Fonksiyonun hesapladığı sonucu dışarıdaki koda geri vermesidir.
"""
def cikar(x, y):
    return x - y # Hesaplanan sonucu geri döndürür.

sonuc = cikar(10, 5) # sonuc değişkeni 5 olur.
"""

# Return ile Hata Kontrolü:
# Fonksiyon, bir sorun olduğunda özel bir değer döndürerek işlemi durdurabilir.
"""
def bol(x, y):
    if y == 0:
        return "Hatalı işlem (0'a bölünemez)"
    else:
        return x / y

print(bol(12, 0)) # Çıktı: "Hatalı işlem..."
"""

# Değişken Kapsamı (Scope):
# global: Fonksiyonun *dışında* tanımlanan, her yerden erişilebilen değişken.
# local: Fonksiyonun *içinde* tanımlanan, sadece orada geçerli olan değişken.
# `global` Anahtar Kelimesi: Fonksiyonun içinden dışarıdaki (global) bir değişkenin
# değerini zorla değiştirmek için kullanılır (Genellikle tavsiye edilmez).
"""
x = 10 # Global
def ornek2():
    global x # "Dışarıdaki x'i kullanacağım"
    x = x * 3 # Dışarıdaki x'i değiştirir
"""

