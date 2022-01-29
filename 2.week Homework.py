#OTAPARK 1

saat=int(input("otaparkta kaç saat kaldınız?"))
if saat <=1:
    print(5 ,"TL")
elif 1<saat<5:
    print(saat*4)
else:
    print(saat*3)

#2 üçgen
a1=int(input(" 1. kenar uzunluğunu girin"))
a2=int(input(" 2. kenar uzunluğunu girin"))
a3=int(input(" 3. kenar uzunluğunu girin"))             
if a1==a2==a3:
    print("Eşitkenar üçgen")
elif a1==a2 or a1==a3 or a2==a3:
    print("ikizkener üçgen")
else:
    print("Çeşitkenar")
    
#3 zamm
a1=(input(" kullanıc adınız"))
maas=int(input(" Maaşınız"))
yil=int(input(" Çalışma yılınız"))
if 0<=yil<=5:
    print("Sayın " ,a1, "zamlı maaşınız",maas+ maas*0.10,"TL")
elif 6<=yil<=10:
    print("Sayın " ,a1, "zamlı maaşınız",maas+ maas*0.15,"TL")
else:
    print("Sayın " ,a1, "zamlı maaşınız",maas+ maas*0.25,"TL")
  
#4 EN BÜYÜK SAYI BULMA
max=0
a=int(input("1.sayıyı gir"))
if a>max:
     max=a       
b=int(input("2.sayıyı gir"))
if b>max:
     max=b
c=int(input("3.sayıyı gir"))
if c>max:
     max=c
print("max:",max)


#5İNDİRİMM
hang=input(" SİNEMA / TİYATRO")
a=input("öğrenci / sivil ")

if a=="ö":
    if hang=="s":  
        print("7.5 TL")
    elif hang=="t":
        print("5 TL")
else:
    if hang=="s":
        print("15 TL")
    elif hang=="t":
        print("10 TL")       
#6 bölünme
sayi=int(input("sayı giriniz"))
if sayi%3==0 and sayi%5==0:
    print("15’e tam bölünür")
else:
    print(" 15’e tam bölünmez")
    

#7 havayolu
kilo=int(input("bagaj agırlığı"))
if kilo<=20:
    print("Herhangi bir ücret ödemeniz gerekmiyor")
else:
    print("Fazla bagaj için ",(kilo-20)*10," TL ödemelisiniz")

#8 sınav
s1=int(input("sıanv notunuzu girniz"))
s2=int(input("sıanv notunuzu girniz"))
p=int(input("performans notunuzu girniz"))
m=(s1+s2+p)/3
if m>=50:
    print("başarılı",m)
else:
    print("başarısız",m)
    












