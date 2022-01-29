"""
notu = int(input("notunuzu giriniz"))
if notu>100 or notu<0:
    print( "hatalı giriş yaptınız")
else:           
    if notu>=90 and notu <= 100:
            print("AA")
    elif notu>=85 and notu <= 89:
             print("BA")
    elif notu>=80 and notu <= 84:
             print("BB")
    elif notu>=75 and notu<=89:
             print("CB")
    elif notu>=70 and notu<=74:
             print("CC")
    elif notu>=65 and notu<=69:
             print("DC")
    elif notu>=60 and notu<=64:
             print("DD")
    elif notu>=50 and notu<=59:
             print("FD")
    else:
             print("FF")

sayi=int(input("sayı giriniz"))
if sayi%2==0:
    print("çift")
else:
    print("tek")

"""
"""
sayi=int(input("sayı giriniz"))

if sayi>0:
    print("pozitif")
else:
    print("negatif")
               
"""              
"""
kulaniciAd=input("Kullanıcı adını giriniz")
sifre=input("şifre giriniz")
if kulaniciAd=="Türkiye" and   sifre=="1923":
          print("Giriş başarılı")
else:
    print("Kullanıcı adı ve şifre yanlış ")
"""    
          
"""
islemci=input("işlemci bilginizi giriniz")
ram=input("RAM bilginizi giriniz")
if islemci=="i7" or ram=="8gb":
    print("KURULUM UYGUN")
else:
    print("KURULUM UYGUN DEĞİL")
"""   
"""
s1=int(input("1.sayı giriniz"))
s2=int(input("2.sayı giriniz"))
opr=input("operatör girin '+,-,*,/' ")
if opr=="+":
       print(s1+s2)
elif opr=="-":
       print(s1-s2)
elif opr=="*":
       print(s1*s2)
elif opr=="/":
       print(s1/s2)       
       
else:
    print("Yanlış işlem girdiniz")
"""
"""
boy=int(input("Boyunuzu girin:"))
kilo=int(input("Ağırlığınızı girin:"))
vki=kilo/(boy*boy)
print(vki)
if vki>=18 and vki<=25:
print("normal")
elif vki>=26 and vki<=55:
        print("normal üstü")
elif vki>=56 and vki<=70:
        print("obez")
"""
s1=int(input("1.sayıyı giriniz"))
s2=int(input("2.sayıyı giriniz"))
s3=int(input("3.sayıyı giriniz"))
ort=(s1+s2+s3)/3
if ort>=50:
    print("GEÇTİ",ort)
    print(ort)
else:
    print("KALDI",ort)
