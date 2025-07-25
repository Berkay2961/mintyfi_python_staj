#Girilen yaşa göre reşit olup olmadığını kontrol etme
yas=int(input("Yasinizi girin: "))
if yas>=18:
    print("Reşitsiniz.")
else:
    print("Reşit değilsiniz.")  

#Kullanıcıdan alınan nota göre geçti veya kaldı bilgisini yazdırma
notu = int(input("Notunuzu girin: "))
if notu >= 50:
    print("Geçtiniz.")
else:
    print("Kaldınız.")

    #Basit bir sayı tahmin oyunu(sabit sayı ile karşılaştırma)

    sabit_sayi = 7
tahmin = int(input("Bir sayı tahmin edin (1-10): "))
if tahmin == sabit_sayi:
    print("Tebrikler! Doğru tahmin ettiniz.")
elif tahmin < sabit_sayi:
    print("Tahmininiz çok düşük. Daha yüksek bir sayı deneyin.")
else:
    print("Tahmininiz çok yüksek. Daha düşük bir sayı deneyin.")

    #üç sayıdan en büyüğünü bulma
sayi1 = int(input("Birinci sayiyi girin: "))
sayi2 = int(input("İkinci ssayiyi girin: "))
sayi3 = int(input("Üçüncü sayiyi girin: "))
if sayi1 >= sayi2 and sayi1 >= sayi3:
    print("En büyük sayı:", sayi1)
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print("En büyük sayı:", sayi2)
else:
    print("En büyük sayı:", sayi3)

    #sayının pozitif, negatif veya sıfır olduğunu yazdıran kod
    sayi=int(input("Sayiyi girin:  "))
    if sayi>0:
        print("Sayi pozitif.")
    elif sayi<0:
        print("Sayi negatif.")
    else:
        print("Sayi sifir.")