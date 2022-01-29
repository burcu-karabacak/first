
vize=int(input("vize notunuz"))
final=int(input("Final notunuz"))
gecmenotu=vize*0.4 + final*0.6
if gecmenotu>=60:
    print("GEÇTİ")
else:
    print("KALDI")

vize=int(input("vize notunuz"))
final=int(input("Final notunuz"))
gecmenotu=vize*0.4 + final*0.6
if final>60:
    
   if gecmenotu>=60:
       print(gecmenotu,"GEÇTİ")
   else:
       print(gecmenotu,"KALDINIZ MALESEF geçme notunuz düşük")       
else:
    print(gecmenotu,"MALESEF KALDINIZ! çünkü final notunuz düşük")

sayi=int(input("sayı giriniz"))
if sayi>100 or sayi<0:
    print("HATALI GİRİŞ")
else:
    pass

parola=str(input("PAROLA GİRİNİZ"))
uzunluk=len(parola)
if uzunluk<8:
    print("ZAYIF PAROLA GİRDİNİZ")
else:
    print("GÜÇLÜ PAROLA")

notx=int(input("NOTUNUZU GİRİNİZ"))
if notx>=0 and notx<=100:
            if notx>80:
                notx+=10
                if notx>100:
                    notx=100
                    print(notx)
                else:
                    print(notx)
                 
            elif notx>60:
                notx+=5
                print("not+5:",notx)
            elif notx<45:
                notx-=5
                if notx<0:
                    notx=0
                    print(notx)
                else:
                    print(notx)
            else:
                pass
else:
    print("hatalı giriş")
  
