# --- NOTES3.PY: VERİ İŞLEME VE PROJE KALIPLARI ---

### 1. String (Metin) Metotları
# Metinleri temizlemek, değiştirmek ve formatlamak için kullanılır.

# metin.lower(): Tüm harfleri küçük harfe çevirir.
# Örn: player_input = input().lower() (Karşılaştırma için şart)

# metin.upper(): Tüm harfleri büyük harfe çevirir.
# Örn: currency_from = input().upper() (Döviz Çevirici)

# metin.capitalize(): Sadece ilk harfi büyük yapar, gerisini küçültür.
# Örn: print(f"Seçim: {player_input.capitalize()}") (Görünümü düzeltir)

# metin.replace("eski", "yeni"): Metindeki bir kısmı diğeriyle değiştirir.
# Örn: madlib_story = madlib_story.replace("[noun]", cevap) (Mad Libs)

# f-string: Metin içine kolayca değişken yerleştirir.
# Örn: print(f"{amount_value} USD = {converted_amount} TRY")


### 2. Fonksiyon Tanımlama (`def`)
# Kod bloklarını bir isim altında gruplar, tekrar kullanılabilir hale getirir ve düzenler.

# def fonksiyon_adi(): Fonksiyonu tanımlar (Henüz çalıştırmaz).
# Örn: def run_rock_paper_scissors(): ...

# fonksiyon_adi(): Tanımlanan fonksiyonu çalıştırır.
# Örn: run_rock_paper_scissors() (Genellikle kodun en sonunda)


### 3. Veri Eşleştirme (ZIP)
# İki ayrı listeyi (isimler, numaralar) birbirine bağlar.

# list(zip(list1, list2)): İki listeyi alıp tuple (çift) listesi yapar.
# Örn: qa_pair = list(zip(questions, answers)) (Quiz App)

# for a, b in zip_listesi: ZIP'li listede index kullanmadan temiz döngü kurar.
# Örn: for ad, numara in in_pair: ... (En Yüksek Öğrenci)


### 4. En Yüksek Değeri Bulma (İki Yöntem)
# Bir listedeki en yüksek değere karşılık gelen diğer listedeki veriyi bulma.

# Yöntem 1: max() / .index() (En hızlı yöntem)
"""
max_numara = max(numaralar)
max_index = numaralar.index(max_numara)
max_ogrenci = isimler[max_index]
"""

# Yöntem 2: ZIP ve Döngü (Manuel takip)
"""
max_numara = in_pair[0][1] # Başlangıç değeri (ilk öğrencinin numarası)
for ad, numara in in_pair:
    if numara > max_numara:
        max_numara = numara
        max_ogrenci_adi = ad
"""