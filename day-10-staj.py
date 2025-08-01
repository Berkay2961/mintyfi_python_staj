#Kullanıcıdan bilgi al ve .txt dosyasına kaydet
ad = input("Adınız: ")
soyad = input("Soyadınız: ")
yas = input("Yaşınız: ")

with open("kullanici_bilgileri.txt", "w", encoding="utf-8") as dosya:
    dosya.write(f"Ad: {ad}\n")
    dosya.write(f"Soyad: {soyad}\n")
    dosya.write(f"Yaş: {yas}\n")

print("Bilgiler başarıyla 'kullanici_bilgileri.txt' dosyasına kaydedildi.")

#Daha önce kaydedilmiş bir .txt dosyasını satır satır oku
dosya_adi = "kullanici_bilgileri.txt"

try:

    with open(dosya_adi, "r", encoding="utf-8") as dosya:
        print("Dosya içeriği:\n")
        for satir in dosya:
            print(satir.strip()) 
except FileNotFoundError:
    print(f"'{dosya_adi}' dosyası bulunamadı.")

    #Python sözlüğünü .json dosyasına yaz ve tekrar oku
    import json

# Python sözlüğü
kullanici = {
    "ad": "Berkay",
    "soyad": "Şahin",
    "yas": 25,
    "email": "berkay@example.com"
}

# .json dosyasına yaz
with open("kullanici.json", "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya, ensure_ascii=False, indent=4)

print("Sözlük başarıyla 'kullanici.json' dosyasına yazıldı.")

#datetime modülünü kullanarak tarihi dosyaya yaz
from datetime import datetime

# Şu anki tarih ve saat
simdi = datetime.now()

# İsteğe bağlı biçimlendirme (gün-ay-yıl saat:dakika:saniye)
tarih_str = simdi.strftime("%d.%m.%Y %H:%M:%S")

# Dosyaya yazma
with open("tarih_kaydi.txt", "w", encoding="utf-8") as dosya:
    dosya.write(f"Kayıt zamanı: {tarih_str}\n")

print("Tarih ve saat başarıyla 'tarih_kaydi.txt' dosyasına yazıldı.")

#random modülü ile rastgele şifre üreten program yaz
import random

# Şifrede kullanılacak karakterler
harfler = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
rakamlar = "0123456789"
semboller = "!@#$%^&*()_+-=<>?/|"

# Tüm karakterleri birleştir
tum_karakterler = harfler + rakamlar + semboller

# Şifre uzunluğunu belirle
sifre_uzunlugu = 12

# Rastgele şifre oluştur
sifre = "".join(random.choice(tum_karakterler) for _ in range(sifre_uzunlugu))

print("Oluşturulan Şifre:", sifre)