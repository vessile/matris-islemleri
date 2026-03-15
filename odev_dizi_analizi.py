# Bölüm 1 – Kullanıcıdan Veri Alma
n = int(input("Kaç sayı gireceksiniz: "))
dizi = []

for i in range(n):
    sayi = int(input(f"Sayı {i+1}: "))
    dizi.append(sayi)

# Bölüm 2 – Dizi Analizi
toplam = sum(dizi)
ortalama = toplam / n
en_buyuk = max(dizi)
en_kucuk = min(dizi)

print("\nDizi Analizi:")
print("Toplam:", toplam)
print("Ortalama:", ortalama)
print("En büyük sayı:", en_buyuk)
print("En küçük sayı:", en_kucuk)

# Bölüm 3 – Özel Analiz
cift_sayilar = 0
tek_sayilar = 0
on_buyuk_sayilar = 0

for sayi in dizi:
    if sayi % 2 == 0:
        cift_sayilar += 1
    else:
        tek_sayilar += 1
    if sayi > 10:
        on_buyuk_sayilar += 1

print("\nÖzel Analiz:")
print("Çift sayı sayısı:", cift_sayilar)
print("Tek sayı sayısı:", tek_sayilar)
print("10'dan büyük sayı sayısı:", on_buyuk_sayilar)

# Bölüm 4 – Diziyi Ters Yazdırma
print("\nTers Dizi:")
for sayi in reversed(dizi):
    print(sayi, end=" ")
print()

# Bölüm 5 – Sayı Arama
aranacak = int(input("\nAranacak sayı: "))
if aranacak in dizi:
    print("Sayı dizide bulundu")
else:
    print("Sayı dizide bulunamadı")

# Bonus 1 – Negatif sayıları listeleme
negatifler = [sayi for sayi in dizi if sayi < 0]
if negatifler:
    print("Negatif sayılar:", negatifler)
else:
    print("Negatif sayı yok")

# Bonus 2 – Ortalamanın üzerindeki sayılar
ust_ortalama = [sayi for sayi in dizi if sayi > ortalama]
if ust_ortalama:
    print("Ortalamanın üzerindeki sayılar:", ust_ortalama)
else:
    print("Ortalamanın üzerinde sayı yok")
