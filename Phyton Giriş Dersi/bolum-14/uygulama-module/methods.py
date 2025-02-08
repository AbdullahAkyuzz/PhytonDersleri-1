import db

def urunEkle(urunAdi, fiyat):
   db.urunler.append({
       "id":len(db.urunler) + 1,
       "urun Adi":urunAdi,
       "fiyat" : fiyat
   })
   
def urunGuncelle(id,isim,fiyat):
    id = int(id)
    for i in db.urunler:
        if(i["id"]==id ):
            i["urun Adi"]=isim
            i["fiyat"]=fiyat
            break
        
def urunleriGetir():
    for i in db.urunler:
        print(f"ID no {i["id"]} Urun Adi {i["urun Adi"]} Fiyatı {i["fiyat"]}")

def urunleriGetirr():
    urunleriGetir()
    print("----")
         
def urunSil(id):
    a=False
    for i in db.urunler:
        if i["id"] == id:
                db.urunler.remove(i)
                a=True
    if a:
        # ID'leri güncellemek için listedeki tüm elemanları sırayla düzenle
        for index, urun in enumerate(db.urunler, start=1):
            urun["id"] = index  # ID'yi yeni sıraya göre güncelle

        
    