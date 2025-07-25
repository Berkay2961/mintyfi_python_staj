#degisken tanimlama ve ekrana yazdirma

yas=20
boy=1.85
kilogram=90
print("\nYas✔",yas)
print("Boy✔",boy)
print("Kilogram✔",kilogram)


#iki sayi tanimla ve dort islem metni yazdir
sayi1= 18
sayi2 = 22

toplam=sayi1+sayi2
fark=sayi1-sayi2
carpim=sayi1*sayi2
bolum=sayi1/sayi2

print("Toplam",toplam)
print("Fark",fark)
print("Carpim",carpim)
print("Bolum",bolum)

#kullanicidan yas bilgisini alip 5 yil sonraki yasini yazdirma
yas= int(input("Yasinizi girin:"))
gelecekYas= yas+5
print("5 yil sonraki yasiniz:", gelecekYas)


#type fonksiyonuyla farklı veri türlerini yazdırma(bir değişkenin veri türünü öğrenmek için kullanılır)

sayi1 = 10
sayi2 = 3.14
print(type(sayi1))  # int
print(type(sayi2))  # float
metin = "Merhaba"
print(type(metin))  # str
liste = [1, 2, 3]
print(type(liste))  # list
demet = (1, 2, 3)   
print(type(demet))  # tuple
set_veri = {1, 2, 3}
print(type(set_veri))  # set
sozluk = {"ad": "Ahmet", "yas": 30}
print(type(sozluk))  # dict

#tip dönüşüm hataları
sayi =int(12,5)  # Hata: int() fonksiyonu sadece tam sayıları alır, ondalıklı sayıları kabul etmez.
# sayi = int("Merhaba")  # Hata: "Merhaba" metni tam sayıya dönüştürülemez.
# sayi = float("123abc")  # Hata: "123abc" metni float'a dönüştürülemez.
sayi = int((float(12.5)))  # Doğru: float'ı önce int'e dönüştürür.

sayi=int([1, 2, 3])  # Hata: Liste doğrudan int'e dönüştürülemez.

sayi = int({"ad": "Ali"})  # Hata: Sözlük doğrudan int'e dönüştürülemez.