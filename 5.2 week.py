"""
try:
    a=int(input("sayi1 giriniz"))
    b=int(input("sayi2 giriniz"))
    topla=a+b
    print(topla)
except ValueError:
    print("lütfen sadece sayı giriniz")
finally:
    print("iyi günler")
"""
"""
while True:
    s1=input("1.sayı: (çıkmak için e tuşuna basınız)")
    if s1=="e":
        break
    s2=input("2.sayı:")
    
    try:
        a=int(input("sayi1 giriniz"))
        b=int(input("sayi2 giriniz"))
        böl=a/b
        print(böl)
    except ZeroDivisionError:  #except (ZeroDivisionError,ValueError):
        print("bir sayıyı 0'a bölemezsiniz!")  #while döngüsü ekleyerek tekrardan sayı istenebilir
    except ValueError:
        print("lütfen sayılarınızı kontrol edin")
    finally:
        print("işlem yapıldı")
"""       
"""
while True:
    s1=(input("1.sayı: (çıkmak için e tuşuna basınız)")).strip()
    if s1=="e" or s1=="E":
        print("çıktınız")
        break
        
    #s2=input("2.sayı:")
    
    try:
        a=int(input("sayi1 giriniz"))
        b=int(input("sayi2 giriniz"))
        print(a,"/",b,"=",a/b)
    except(ZeroDivisionError,ValueError):#except (ZeroDivisionError,ValueError):
        print("Bir hata meydana geldi. Tekrar deneyiniz")
      
    finally:
        print("işlem yapıldı")
        
"""
"""

while True:
    x=input("bir sayı giriniz")
    if not x:
        break
    try:
        y=1/float(x)
    except ValueError as e1:
        print("geçersiz sayı"+str(e1))
        continue
    except ZeroDivisionError as e2:
        print("sıfıra bölme"+str(e2))
        continue
    print(y)
"""

"""
while True:
    x=input("bir sayı giriniz")
    if not x:
        break
    try:
        y=1/float(x)
    except ValueError as e1:
        print("geçersiz sayı",e1) #, ile bağladık
        continue
    except ZeroDivisionError as e2:
        print("sıfıra bölme",e2)
        continue
    print(y)

"""

try:
    y=float(input("sayı girin"))
    a=y**1000
    print(a)
except OverflowError as e:
    print("işlem çok büyük",e)
except ZeroDivisionError as e1:
    print("Sıfıra bölme",e1)


















    

