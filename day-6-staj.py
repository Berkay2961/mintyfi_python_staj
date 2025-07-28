# tuple içine haftanın günlerini tanımla ve ilk 3 günü yazdır

haftanin_gunleri = ("Pazartesi","Salı","Çarşamba","Perşembe","Cuma","Cumartesi","Pazar")
print(haftanin_gunleri[:3])

# kullanıcının girdiği kelimelerden oluşan listede tekrar edenleri set ile ayıkla

kelimeler = input("Lütfen kelimeleri giriniz (virgülle ayırın):")
kelime_listesi = kelimeler.split(",")
tekrar_edenler = set(kelime_listesi)
print("Tekrar eden kelimeler:", tekrar_edenler)

# 2 farklı set ile kesişim , birleşim ve fark işlemlerini yap

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
kesisim = set1.intersection(set2)
birlesim = set1.union(set2) 
fark = set1.difference(set2)
print("Kesişim:", kesisim)
print("Birleşim:", birlesim)    
print("Fark:", fark)

# bir string içindeki benzersiz (tekrarsız) karakterleri set kullanarak göster
string = "Merhaba Dünya"
benzersiz_karakterler = set(string)
print("Benzersiz karakterler:", benzersiz_karakterler)

# tuple kullanarak doğum tarihi(gün,ay,yıl) bilgisi tanımla
dogum_tarihi = (3,6,2005)
print("Doğum tarihi:", dogum_tarihi)



                
