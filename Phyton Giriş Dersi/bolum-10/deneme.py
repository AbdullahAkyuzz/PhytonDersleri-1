# 1- Kendisine gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazınız. 

def ekranda(kelime,sayi):
    return kelime*sayi
print(ekranda("Abdullah",2))
# 2- Dikdörgenin alan ve çevresini hesaplayan fonksiyonu yazınız.



# 3- Yazı tura uygulamasını fonksiyon kullanarak yapınız. (Random modülü)


# 4- Kendisine gönderilen 2 sayı arasındaki tüm asal sayıları bulan fonksiyonu yazınız.

def asalSayiBul(sayi1,sayi2):
    for sayi in range(sayi1,sayi2+1):
        if(sayi>1):
            for i in range(2,sayi):
                if(sayi % i ==0):
                    break
            else:
                print(sayi)
 
        

# 5- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazınız.


                
