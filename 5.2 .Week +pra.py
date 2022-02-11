"""
a=0
b=[]#boş liste tanımladı
sayi=0 #değişken olarak
while a<10:  #len(b)<10 de olur
    a=a+1
    try:
        sayi=int(input("Sayı girin"))
    except ValueError:
        print("hatalı giriş")
        sayi=0
        a=a-1
    if sayi>0:
        b.append(sayi)
    elif sayi<0:

        break
print(b)
"""

"""
b=[]
for i in range(1,11):
    try:
        print("sayı:",i)
        sayi=int(input("Sayı girin"))
        
    except ValueError:
        print("hatalı giriş")
        print("sayı:",i)
        sayi=int(input("Sayı girin"))
    if sayi>0:
        
        b.append(sayi)
    else:
        break
print(b)
b.sort()
print(b)
"""
"""
fo = open("dosya.txt", "r+")
print(fo.read())
fo.close()
"""
"""
dosya=open("kitap1.xslx","a")
dosya.write(" /n burcudsndjk ")
dosya.closed()
print(dosya.read())
"""
dosya=open("dosyaa.txt","r+")
yazi=input("adınızı giriniz")
dosya.write(yazi+"\n")
dosya.close()
dosya=open("dosyaa.txt","r+")
print(dosya.read())
dosya.close()
# a	Eklemek için bir dosya açar. Dosya varsa dosya işaretçisi dosyanın sonundadır. Dosya mevcut değilse, yazmak için yeni bir dosya oluşturur.
# w	Sadece yazmak için bir dosya açar. Dosya varsa, dosyanın üzerine yazar. Dosya yoksa, yazmak için yeni bir dosya oluşturur.
#r	Sadece okumak için bir dosya açar. Dosya işaretçisi, dosyanın başına yerleştirilir. Bu varsayılan moddur.
#r+	Hem okuma hem de yazma için bir dosya açar.











