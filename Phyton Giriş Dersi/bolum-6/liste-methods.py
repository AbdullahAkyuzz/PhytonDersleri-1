sayilar = [4,6,8,2,56,78,90,4,4]
isimler = ['ahmet','canan','zeynep','gökhan','ali','canan']

sonuc = min(sayilar)
sonuc = min(isimler)
sonuc = max(isimler)
sonuc = max(sayilar)

# ekleme
# sayilar.append(12)
# isimler.append('çınar')

# sayilar.insert(0, 100)       0.değere 100ü ata Not: değişim yapmaz yeni eleman ekler 
# sayilar.insert(-1, 100)      sonuncu değere 100ü ata   not: sondan bir öncesine atar
# sayilar.insert(-3, 100)      önce sağa kaydırır sonra ekler 
# sayilar.insert(len(sayilar), 100)  len(sayılar)=sonuncu değer 

# silme
# sayilar.pop()                defaultu -1 dir yani liste sonundan siler 
# sayilar.pop(0)                pop indexse göre remove arama yaparak 
# isimler.remove('canan')

# sıralama
# sayilar.sort()                Kucukten buyuge artar 
# isimler.sort()
# sayilar.reverse()             Tersten sıralar 

# arama
sonuc = sayilar.index(4)

# sonuc = sayilar.count(4)
# sonuc = isimler.count('canan')

print(sonuc)