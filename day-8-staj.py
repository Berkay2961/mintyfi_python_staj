#iki sayının toplamını döndüren fonksiyon
def topla (sayi1, sayi2):
    return sayi1 + sayi2

#girilen iki sayını asal olup olmadığını kontrol eden fonksiyon
def asal_mi(sayi):
    if sayi < 2:
        return False
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            return False
    return True

#liste içindeki sayıların ortalamasını hesaplayan fonksiyon
def ortalama(liste):
    if len(liste) == 0:
        return 0
    return sum(liste) / len(liste)

#metni ters çeviren bir fonksiyon yaz
def ters_cevir(metin):
    return metin[::-1]

#parametre olarak liste alıp karesini alan fonksiyon
def kare_al(liste):
    return [x**2 for x in liste]





