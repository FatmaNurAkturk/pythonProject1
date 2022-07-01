"""
1-Kullanıcıdan aldığınız 3 tane sayıyı çarparak ekrana yazdırın. Ekrana yazdırma işlemini format metoduyla yapmaya çalışın.

s1=int(input("Birinci Sayı:"))
s2=int(input("İkinci Sayı:"))
s3=int(input("Üçüncü sayı:"))

carpım=s1 * s2 * s3

print("{} * {} * {} = {}".format(s1,s2,s3,carpım))


2-Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)


boy = float(input("Boyunuzu Girin:"))
kilo= int(input("Kilonuzu Girin:"))

bki = kilo / (boy * boy)

print("Beden Kitle İndeksiniz: {}\n".format(bki))

3-Bir aracın kilometrede ne kadar yaktığı ve kaç kilometre yol yaptığı bilgilerini alın ve
sürücünü toplam ne kadar ödemesini gerektiğini hesaplayın.
"""
"""
kmyakar=int(input("Arac Kilometrede ne kadar yakar:"))
kackm=int(input(("Arac kaç km yol yapar: ")))

tutar=kmyakar * kackm

print("Toplam Tutar: {}".format(tutar))

4-Kullanıcıdan ad,soyad ve numara bilgisini alarak bunları alt alta ekrana yazdırın.

ad = input("Ad:")
soyad=input("Soyad:")
numara=int(input("Telefon Numarası:"))

print("Bilgileriniz.....")

print("Ad: {}\nSoyad: {}\nTelefon Numarası: {}\n".format(ad,soyad,numara))

5- Kullanıcıdan iki tane sayı isteyin ve bu sayıların değerlerini birbirleriyle değiştirin.


d1=int(input("A"))
d2=int(input("B"))

print("Değiştirilmeden Önceki Değerler:\nA:{}\nB:{}".format(d1,d2))


yenideger= d1,d2=d2,d1

print("Değiştirildikten Sonraki Değerleriniz:{}".format((yenideger)))


6-Kullanıcıdan bir dik üçgenin dik olan iki kenarını(a,b) alın ve hipotenüs uzunluğunu bulmaya çalışın.
Hipotenüs Formülü: a^2 + b^2 = c^2


k1=int(input("Birinci Kenar:"))
k2=int(input("İkinci Kenar:"))
hipotenüs=(k1 ** 2 + k2 **2)**0.5

print("Hipotenüs:{}".format(hipotenüs))
"""


