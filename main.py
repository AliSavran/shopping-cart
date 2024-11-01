class urun:

    def __init__(self,ad,fiyat,stok):

        self.ad = ad
        self.fiyat = fiyat
        self.stok = stok

    def __str__(self):
        return "{} - Fiyat: {} TL, Stok: {}".format(self.ad, self.fiyat, self.stok)

class Alışveriş_sepeti:

    def __init__(self):
        self.urunler = []

    def urun_ekle(self,urun):
        self.urunler.append(urun)

    def toplam_tutar(self):

        return sum(urun.fiyat for urun in self.urunler)

    def sepeti_listele(self):
        for urun in self.urunler:
            print(urun)

sepet = Alışveriş_sepeti()

urun1 = urun("Laptop", 30000, 100)
urun2 = urun("Akıllı Telefon", 25000, 150)
urun3 = urun("Tablet", 12000, 50)
urun4 = urun("Kamera", 7800, 15)
urun5 = urun("Tv", 14500, 45)


sepet.urun_ekle(urun1)
sepet.urun_ekle(urun2)
sepet.urun_ekle(urun3)
sepet.urun_ekle(urun4)
sepet.urun_ekle(urun5)


print("Alışveriş Sepeti:")
sepet.sepeti_listele()
print("\nToplam Tutar: {} TL".format(sepet.toplam_tutar()))
