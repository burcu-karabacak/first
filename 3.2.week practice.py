#####
"""
sayilar=[10,23,-5,0,4,-8,-1,3,-9]
toplam=0
negsay=0
for sayi in sayilar:
    if sayi>0:
        toplam=toplam+sayi
    elif sayi<0:
        negsay=negsay+1
print("pozitif sayıların toplamı:",toplam)
print("negatif sayıların sayısı:",negsay)
"""
"""
carpim=1
for i in reversed(range(1,5)):
    carpim=carpim*i
print(carpim)
"""
#####
""""
i=1
sonuc=1
fak=int(input("Faktoriyeli hesaplanacak sayıyı giriniz: "))
while (i<=fak):
 sonuc=i*sonuc
 i=i+1
print("Sonuc=" ,sonuc)
"""
"""
a=int(input(" sayıyı giriniz: "))
b=int(input(" sayıyı giriniz: "))
for i in range(a,b+1):
    print(i)
"""
"""
a=int(input(" sayıyı giriniz: "))
b=int(input(" sayıyı giriniz: "))
if a<b:
    for i in range(a,b+1):
        print(i)
else:
    for i in range(a,b-1,-1):
       print(i)
"""
#####
sayi1=int(input("1sayı yaz:"))

sayi2=int(input("2sayi yaz:"))
if sayi1>sayi2:
    sayi1,sayi2=sayi2,sayi1
#if le while bağımsız
while sayi1<sayi2:
    print(sayi1)
    sayi1+=1
