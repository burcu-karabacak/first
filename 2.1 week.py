"""
s1=int(input("sayı 1 gir"))
s2=int(input("sayı 2 gir"))

if s1<s2:
    print( "s1 <s2")
    print(s1,"<",s2)
elif s1>s2 :
    print(s1,">", s2)

else:
    print(" s1 = s2 ")
    print(s1,"=",s2)
 """
"""

s1=int(input("sayı 1 gir"))
s2=int(input("sayı 2 gir"))

if s1<s2:
    print( "s1 <s2")
    print(s1,"küçüktür",s2)
elif s1>s2 :
    print(s1,"büyüktür", s2)

else:
    print(" s1 eşittir s2 ")
    print(s1,"=",s2)
"""

#ör 2 kullanıcıdan 0-100 arası sayı iste
#80-100  iyii
#45-79    orta
#0-44      kötüü

"""
sayi=int(input(" Sayı Giriniz:"))
if sayi > 100 or sayi < 0:
    print("hatalı giriş yaptınız")

elif sayi >=80 and sayi <= 100:
    print("İYİ")
elif sayi >= 45 and sayi<=79:
    print("ORTA")
else:
    print("KÖTÜ")


"""
"""
s1=int(input("sayı 1 gir"))
s2=int(input("sayı 2 gir"))
ort=(s1 + s2 )/2
#print(int(ort))
if s1<30 or s2<30:
    print("kaldı")
else:
    if ort>=50:
        print("GEÇTİ")
    else:
        print("KALDI")
"""

"""
# yA DA
s1=int(input("sayı 1 gir"))
s2=int(input("sayı 2 gir"))
ort=(s1 + s2 )/2
if (s1 >=30 and s2>= 30):
    if ort>=50:
        print("GEÇTİ")
    else:
        print("KALDI")
else:
    print(" KALDI")

"""
"""
yıl=int(input("yıl girimiz"))
bol=yıl%4
#print(int(bol))
if bol==0:
    print("366  gün var")
else:
    print("365 gün var")

"""
"""" BENİM YAPTIĞIM
s1=int(input("sayı1 girin"))
s2=int(input("sayı2 girin"))
s3=int(input("sayı3 girin"))

if s1>s2 and s1>s3:
    print("EN BÜYÜK",s1)
elif s2>s1 and s2>s3:
       print("EN BÜYÜK",s3)
else:
    print("EN BÜYÜK",s3)
"""    

#sayi1 = int(input("1. Sayı: "))

#sayi2 = int(input("2. Sayı: "))
#
sayi3 = int(input("3. Sayı: "))


#if (sayi1 >= sayi2) and (sayi1 >= sayi3):
   buyuk = sayi
#1
elif (sayi2 >= sayi1) and (sayi2 >= sayi3):
   buyuk = sayi2

#else:
   buyuk = sayi3


#print(sayi1,",",sayi2,"ve",sayi3,"içinde büyük olan sayı",buyuk)
max=0
a=int(input("1.sayıyı gir))
if a>max:
     max=a       
b=int(input("2.sayıyı gir))
if b>max:
     max=b
c=int(input("3.sayıyı gir))
if c>max:
     max=c
print("max:",max)
AA	90-100	
	BA	85-89	
	BB	80-84	
	CB	75-79	
	CC	70-74	
	DC	65-69	
	DD	60-64	
	FD	50-59	
	FF	0-49


