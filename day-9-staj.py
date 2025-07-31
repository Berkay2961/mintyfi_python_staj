#sıfıra bölme hatasını yakalayan program
try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = sayi1 / sayi2
    print("Sonuç:", sonuc)

except ZeroDivisionError:
    print("Hata: Bir sayı sıfıra bölünemez!")

except ValueError:
    print("Hata: Lütfen sadece sayı girin.")

finally:
    print("İşlem tamamlandı.")


#kullanıcının sayı girmesini isteyen ama metin girerse uyarı veren kod
while True:
    try:
        sayi = float(input("Bir sayı girin: "))
        print("Teşekkürler! Girdiğiniz sayı:", sayi)
        break  
    except ValueError:
        print("Hata: Geçerli bir sayı girin lütfen!")

# liste dışında index vermeye çalışan kodda hata yakala
liste = [1, 2, 3, 4, 5]
try:
    index = int(input("Lütfen bir indeks girin (0-4 arası): "))
    print("Liste elemanı:", liste[index])
except IndexError:
    print("Hata: Girilen indeks liste sınırları dışında!")


# Hataları log dosyasına yazdıran basit sistem kur
logging.basicConfig(
    filename="log.txt",      
    level=logging.ERROR,        
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    sayi1 = int(input("Birinci sayıyı girin: "))
    sayi2 = int(input("İkinci sayıyı girin: "))
    sonuc = sayi1 / sayi2
    print("Sonuç:", sonuc)

except ZeroDivisionError as e:
    print("Hata: Bir sayı sıfıra bölünemez!")
    logging.error("Sıfıra bölme hatası: %s", e)

except ValueError as e:
    print("Hata: Lütfen geçerli bir sayı girin!")
    logging.error("Geçersiz giriş hatası: %s", e)

except Exception as e:
    print("Beklenmeyen bir hata oluştu.")
    logging.error("Bilinmeyen hata: %s", e)
import logging

# finally bloğu ile her durumda çalışan kod bloğu örneği yap

try:
    sayi = int(input("Bir sayı girin: "))
    sonuc = 10 / sayi
    print("Sonuç:", sonuc)

except ZeroDivisionError:
    print("Hata: Sıfıra bölme yapılamaz!")

except ValueError:
    print("Hata: Geçersiz giriş, lütfen bir sayı girin!")

finally:
    print("Program tamamlandı, finally bloğu çalıştı.")








