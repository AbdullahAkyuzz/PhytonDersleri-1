"""
** BankaHesabi isminde bir sınıf tanımlayınız.
** Üretilen her bir nesne "hesapSahibi" isminde biz özelliğe sahip olmalıdır. BankaHesabi("Sadık Turan")
** Üretilen her bir nesne "bakiye" isminde bir özelliğe sahip olup başlangıçta 0.0 değerinde olmalıdır.
** Üretilen her bir nesne için "paraYatir" metodu oluşturun ve dışarıdan yatırılacak miktar bilgisini alıp bakiye
   üzerine ekleyin ve bakiye miktarını geriye döndürün.
** Üretilen her bir nesne için "paraCek" metodu oluşturun ve dışarıdan çekilecek miktar bilgisini alıp bakiye
   değerinden çıkarıp geriye döndürün.

    hesap = BankaHesabi("Sadık Turan")
    hesap.hesapSahibi => Sadık Turan
    hesap.bakiye => 0.0
    hesap.paraYatir(1000) => 1000.0
    hesap.paraCek(500) => 500.0
"""

class BankaHesabi:
    def __init__(self, hesapSahibi):
        self.hesapSahibi = hesapSahibi
        self.bakiye = 0.0

    

    def paraYatir(self, miktar):
        self.bakiye += miktar
        return self.bakiye
    
    def paraCek(self, miktar):
        self.bakiye -= miktar
        return self.bakiye
    
    def isimGetir(self):
        return self.hesapSahibi
    
    def get_bakiye(self):
        return self.bakiye
    
hesap = BankaHesabi("Abdullah AKYÜZ")
hesap1 = BankaHesabi("Enes AKYÜZ")

hesap.paraYatir(1000)
print(hesap.get_bakiye())
hesap.paraCek(500)
print(hesap.get_bakiye())
hesap.paraCek(200)
print(hesap.isimGetir())
print(hesap.get_bakiye())

print(hesap1.isimGetir())
print(hesap1.get_bakiye())

hesap1.paraYatir(750)
print(hesap1.isimGetir())
print(hesap1.get_bakiye())



