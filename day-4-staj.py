#1 den 100 e kadar olan tek sayıları yazdırma
for i in range(1, 101):
    if i % 2 != 0:
        print(i, end=" ")

        #kullancıdan 5 sayı alıp bu sayıların  ortalamasını hesaplama
sayi_listesi = []
for i in range(5):
    sayi = float(input(f"{i + 1}. sayiyi girin: "))
    sayi_listesi.append(sayi)
ortalama = sum(sayi_listesi) / len(sayi_listesi)
print("Girilen sayilarin ortalamasi:", ortalama)

#1 den 10 a kadar çarpım tablosunu yazdır
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    
    # 100 e kadar olan sayıların toplamını hesaplama
toplam = 0
for i in range(1, 101):
    toplam += i 
print(" 100'e kadar olan sayıların toplamı:", toplam)

# kullanıcının girdiği sayıya kadar olan çift sayıları listeleme
sayi = int(input("Bir sayi girin: "))
cift_sayilar = []
for i in range(2, sayi + 1, 2):
    cift_sayilar.append(i)
print("Girilen sayıya kadar olan çift sayılar:", cift_sayilar)
