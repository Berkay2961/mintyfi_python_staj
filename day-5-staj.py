# isimlerden oluşan bir liste oluştur ve 3 farklı isim ekle
isimler=["Berkay","Aysun","Ali"]
print("İsimler listesi:", isimler)

#listenin ilk ve son elemanını yazdır
print ("listenin ilk elemani:", isimler[0])
print("listenin son elemanı:", isimler[-1])

#listeyi tersine çevir ve sırala
isimler.reverse()
print("tersine çevrilmiş liste:", isimler)
isimler.sort()
print("sıralanmış hali ile liste:", isimler)

#içinde hem sayı hem string olan karma bir liste oluştur
karma_liste=[5,"Berkay",8,"Şahin",10,"Python",11]
print("karma liste:",karma_liste)

#listenin ortasındaki elemanı silen program
uzunluk = len(karma_liste)
orta_index = uzunluk // 2
del karma_liste[orta_index]
print("Ortadaki eleman silindikten sonra liste:", karma_liste)