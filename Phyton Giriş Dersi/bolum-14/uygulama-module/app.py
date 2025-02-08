# db.pyde ürünler tanıtıldı , metods.py de ise metodlar tanıtıldı 
import methods as m
import db

deger=1
while (not deger==500):
    print("\n1- Urunleri Göser \n2- Urun Ekle \n3- Urun Sil \n4- Urun Guncelle \n5- Cıkış Yap\n")

    deger = input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz: ")
    if(deger=="1"):
        
        m.urunleriGetirr()
        
    elif(deger=="2"):
        
        isim=input("Lütfen Eklemek İsetdiğiniz Telefon Markasını Giriniz: ")
        fiyat=input("Lütfen Eklemek İstediğiniz Telefonun Fiyatını Giriniz: ")
        m.urunEkle(isim,fiyat)
        print(f"\nBaşarıyla {isim} markalı telefon eklendi.")

    elif deger == "3":
        id = input("Lütfen Silmek İstediğiniz Telefon Idsini Giriniz: ")
        id = int(id)  #  ID'yi `int` türüne çevir
        if 1 <= id <= len(db.urunler):  #  ID'nin geçerli olup olmadığını kontrol et
                m.urunSil(id)  
                print(f"\nBaşarıyla {id} ID'li telefon silindi.")
        else:
                print("\n⚠️ HATA: Geçersiz ID numarası! Lütfen tekrar deneyin.")

            

        
    elif(deger=="4"):
        id=input("Lütfen Değiştirmek İsetediğiniz Telefon Idsini Giriniz: ")
        id = int(id)
        if 1 <= id <= len(db.urunler):
            isim=input("Lütfen Yeni Telefon Markasını Giriniz: ")
            fiyat=input("Lütfen Yeni Telefonun Fiyatını Giriniz: ")
            m.urunGuncelle(id,isim,fiyat)
            print(f"\nBaşarıyla {id} idli telefon değiştirildi.")
        else :
            print("\n⚠️ HATA: Geçersiz ID numarası! Lütfen tekrar deneyin.")

    elif(deger=="5"):
        print(f"\nÇıkış Yapılıyor Teklar Bekleriz.")
        SystemExit()
    
