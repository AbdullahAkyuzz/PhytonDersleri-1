customers = ["sadikturan","ahmetyilmaz","cinarturan","yigitbilgi"]
order_totals = [12000,13000,5000,15000]

# 1- 'sadikturan' kullanıcı adıyla yapılan 5000 liralık siparişi listeye ekleyiniz.
customers.append("sadikturan")
order_totals.append(5000)

# 2- Son eklenen siparişi siliniz.
customers.pop()
order_totals.pop()

# 3- Tüm müşteriler için aşağıdaki özet cümleyi yazdırınız.
    # '<username>' isimli müşterinin sipariş toplamı '<10000>' liradır. (döngüler)
sonuc= f"{customers[0]}isimli müşterinin sipariş toplamı {order_totals[0]}"
sonuc= f"{customers[1]}isimli müşterinin sipariş toplamı {order_totals[1]}"
sonuc= f"{customers[2]}isimli müşterinin sipariş toplamı {order_totals[2]}"
sonuc= f"{customers[3]}isimli müşterinin sipariş toplamı {order_totals[3]}"


# 4- Müşterileri alfabetik olarak sıralayınız.
sonuc=customers.sort()

# 5- Sipariş toplamlarını azalan şekilde sıralayınız.
sonuc=order_totals.sort()
sonuc=order_totals.reverse()


# 6- En düşük sipariş hangisidir?
sonuc=order_totals[-1]

# 7- 'sadikturan' isimli kullanıcının kaç tane siparişi vardır?
sonuc=customers.count("sadikturan")

# 8- Customers listesinden 'ahmetyilmaz' isimli kullanıcıyı siliniz.
sonuc=customers.remove("ahmetyilmaz")
sonuc=customers

# 9- Listelerdeki tüm içerikleri siliniz.
sonuc=customers.clear()

# 10- Kullanıcıdan aldığınız kullanıcı adı ve sipariş toplamlarını listeye ekleyiniz.

username = input("Musteri adi giriniz ")
toplam = input("Toplam degeri giriniz ")

customers.append(username)
order_totals.append(toplam)

print(sonuc)
print(customers)
print(order_totals)
print(sonuc)

