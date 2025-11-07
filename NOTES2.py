# --- NOTES2.PY: LİSTELER, DÖNGÜLER VE AKIŞ ---

### 1. Liste Metotları
# Listeler, verileri bir arada tutan kutulardır.

# len(liste): Listenin kaç elemanı olduğunu söyler.
# Örn: print(len(sehirler))

# liste.append("yeni"): Listenin sonuna TEK BİR eleman ekler.
# Örn: Your_list.append(add_task) (To-Do List)

# liste.remove("deger"): Listeden DEĞERE GÖRE ilk bulduğunu siler.
# Örn: Your_list.remove(delete_task) (To-Do List)

# liste.extend(["a", "b"]): Listeye BİRDEN FAZLA eleman ekler.
# Örn: sehirler.extend(["Trabzon", "Konya"])

# liste.pop(index): Belirtilen INDEX'teki elemanı siler ve onu sana verir.
# Örn: cikarilan = sehirler.pop(2)

# liste.sort(): Listeyi A'dan Z'ye veya küçükten büyüğe sıralar.
# Örn: sehirler.sort()


### 2. Döngüler (Tekrar Etme)
# Kod bloklarını tekrar tekrar çalıştırır.

# while True: Sonsuz döngü başlatır. Durması için `break` gerekir.
"""
while True:
    playagain = input("Do you want to roll again? (y/n): ")
    if playagain != 'y':
        break
"""
# (Proje: Zar Atma / TPS Oyunu)

# for ... in koleksiyon: Bir koleksiyondaki (liste, range) her elemanı tek tek gezer.
# Örn: for meyve in meyveler: print(meyve)

# range(start, stop, step): `for` döngüsü için sayı dizisi üretir.
# Örn: for sayi in range(1, 101): toplam += sayi (1'den 100'e kadar)


### 3. Akış Kontrolü (Döngü Yönetimi)
# Döngülerin içindeki akışı kontrol eder.

# break: İçinde bulunduğu döngüyü TAMAMEN DURDURUR.
# Örn: if player_input == 'exit': break (TPS / To-Do List)

# continue: Döngünün o anki adımını ATLAR, bir sonrakine geçer.
# Örn: if player_input not in OPTIONS: continue (TPS - Geçersizse başa dön)


### 4. Random Modülü (import random)

# random.randint(1, 6): İki sayı (dahil) arasında rastgele TAM SAYI seçer.
# Örn: result = random.randint(1, 6) (Zar Atma)

# random.choice(liste): Bir listeden rastgele BİR ELEMAN seçer.
# Örn: computer_choice = random.choice(OPTIONS) (TPS / Kelime Oyunu)

# random.shuffle(liste): Bir listeyi YERİNDE karıştırır (değer döndürmez!).
# Örn: random.shuffle(qa_pair) (Quiz App)