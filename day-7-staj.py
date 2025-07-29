# bir öğrencinin adı, yaşı, notu gibi bilgileri tutan sözlük oluşturma
ogrenci = {
    "ad": "Ahmet",
    "soyad": "Yılmaz",
    "sinif": "10A",
    "yas": 17,
    "not": 85
}
print("Öğrenci Bilgileri:")
print("Ad: {ogrenci['ad']}")
print("Soyad: {ogrenci['soyad']}")
print("Sınıf: {ogrenci['sinif']}")
print("Yaş: {ogrenci['yas']}")
print("Not: {ogrenci['not']}")

#girilen bir kelimenin harf frekanslarını sözlükle sayma
kelime = input("Bir kelime girin: ")
harf_frekansi={}
for harf in kelime:
    if harf in harf_frekansi:
        harf_frekansi[harf] += 1
    else:
        harf_frekansi[harf] = 1
print("Harf Frekansları:", harf_frekansi)

#telefon rehberi gibi çalışan bir sözlük oluşturma
rehber={
    "Ahmet": "555-1234",
    "Mehmet": "555-5678",
    "Ayşe": "555-8765",
    "Fatma": "555-4321"
}
print("Telefon Rehberi:")
for isim, numara in rehber.items():
    print(isim, "->", numara)

    aranan_isim = input("Aramak istediğiniz ismi girin: ")
    if aranan_isim in rehber:
        print(aranan_isim, "numarası:", rehber[aranan_isim])
else:
    print("Bu kişi rehberde bulunamadı.")

    #kullanıcıdan ürün adı ve fiyat alarak bir alışveriş listesi sözlüğü oluşturma
alisveris_listesi = {}
urun_sayisi = int(input("Kaç ürün eklemek istiyorsunuz? "))
for i in range(urun_sayisi):
    urun = input(f"{i+1}. ürünün adını girin: ")
    fiyat = float(input(f"{urun} ürününün fiyatını girin: "))
    alisveris_listesi[urun] = fiyat
print("Alışveriş Listesi:")
for urun, fiyat in alisveris_listesi.items():
    print(f"{urun}: {fiyat:.2f} TL")

    #tüm sözlük anahtarlarını ve değerlerini ayrı ayrı yazdır
print("\nÜrünler:")
for urun in alisveris_listesi.keys():
    print(urun)
print("\nFiyatlar:")
for fiyat in alisveris_listesi.values():
    print(fiyat)









