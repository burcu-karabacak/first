
#1 soru 1)	Klavyeden girilen bir sayının rakamlarını toplayan program
a=int(input("enter your number Please!!!"))
toplam=0
for i in str(a):
    toplam+=int(i)
print("rakamların toplamı:", toplam)

#2 Klavyeden girilen bir cümledeki kelimeleri sayan program

a=input("cümle giriniz")
bosluk=0
for i in a:
    if i==" ":
        bosluk+=1
print("boşluk sayısı:",bosluk)        
print("kelime sayısı:",bosluk+1)
print("harf sayısı:",len(a)-bosluk)

#3 Klavyeden girilen bir sayının faktöriyelini hesaplayan programın 
a=int(input(" sayı giriniz "))
carpım=1
for i in range(1,a+1):
    carpım=carpım*(i)
print("faktöriyel:",carpım)    

##4 Random kullanarak rastgele 0 ile 100 arasında 10 sayı üretiniz.

import random
s=random.random()  # 0-1 arası sayı
print(s)
s2=random.randint(0,100)  #0-100 arası sayı 
print(s2)  #randint(baş,bitiş)

#print(dir(random))
s3=random.uniform(1.4,2.7)
print("sayı3=",s3)

# listeden ratgele alma ise
list=[5,3,6,9,15,20,"bilişim"]
deger=random.choice(list)
print(deger)



