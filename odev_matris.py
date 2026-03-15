# Bölüm 1 – Matris Boyutu Alma
n = int(input("Matris boyutu (n): "))

matris = []

print("Matris elemanlarını giriniz:")

for i in range(n):
    satir = list(map(int, input().split()))
    matris.append(satir)

# Bölüm 2 – Matrisi Yazdırma
print("Matris:")
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
    print()

# Bölüm 3 – Matris Toplamı
toplam = 0

for satir in matris:
    for eleman in satir:
        toplam += eleman

print("Matris toplamı:", toplam)

# Bölüm 4 – Ana Köşegen
print("Ana köşegen:")

for i in range(n):
    print(matris[i][i])

# Bölüm 5 – En Büyük Eleman
en_buyuk = matris[0][0]

for satir in matris:
    for eleman in satir:
        if eleman > en_buyuk:
            en_buyuk = eleman

print("Matrisin en büyük sayısı:", en_buyuk)

# Bölüm 6 – Satır Toplamları

for i in range(n):
    satir_toplami = 0
    for j in range(n):
        satir_toplami += matris[i][j]
    print(f"{i+1}. satır toplamı:", satir_toplami)


# BONUS 1 – En Küçük Eleman
en_kucuk = matris[0][0]

for satir in matris:
    for eleman in satir:
        if eleman < en_kucuk:
            en_kucuk = eleman

print("Matrisin en küçük sayısı:", en_kucuk)


# BONUS 2 – Sütun Toplamları

for j in range(n):
    sutun_toplami = 0
    for i in range(n):
        sutun_toplami += matris[i][j]
    print(f"{j+1}. sütun toplamı:", sutun_toplami)


# BONUS 3 – Matrisi Ters Yazdırma
print("Ters Matris:")

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        print(matris[i][j], end=" ")
    print()


# BONUS 4 – Çift Sayıları Listeleme
print("Matris içindeki çift sayılar:")

for satir in matris:
    for eleman in satir:
        if eleman % 2 == 0:
            print(eleman, end=" ")
          
