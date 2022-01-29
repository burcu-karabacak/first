#1-10 arası toplamı
#for sayi in range(1,10):,

"""kullanıcı negatif bir sayı girinceye kadar giriken sayıları toplar"""
"""
toplam=0
sayi=1
while sayi>=0:
    sayi=int(input("sayı girin"))
    if sayi<0:
        break
    else:
        toplam=toplam+sayi
        print("toplam",toplam)
   
toplam=0
sayi=1
while True:
    sayi=int(input("sayı girin")) # içerde olması gerekir yoksa yukarda döngüyü sonsuza sokar!
    if sayi<0:
        break   # sonsuz döngüye girer!
    else:
        toplam=toplam+sayi
        print("toplam",toplam)

ad=input("isminizi girin")
for i in range(6):
    print(ad,end="")
#print içerisine atama operatörü atamayız    
"""
"""
ad=input("isminizi girin")
for i in reversed(ad):
    print(i,end="")
"""
"""
ad=input("isminizi girin")
for i in range(1,6):
    print(ad) #print(ad,end="")
"""
"""
ters=""
ad=input("isminizi girin")
for i in reversed(ad):
    ters+=ad
print(ters)   

sayi=int(input("yupe your number:"))
for i in range(2,sayi):
    if sayi%i==0:
        print(sayi,i,"ye tam bölünür , asal değil")
        break
else:
    print("asal sayıdır")
#çarpım tablosu    """
"""
for i in range (1,11):
    for j in range(1,11):
        print(i,"x",j,"=",i*j)
    print("_"*10)    #aralarına çizgi çektikk    
print("işlem biiti")
"""
#pc oyunu sayı tutturma
gizlisay=77
Print=input("aklından bir sayı tuttum Tahmin et bakalım")
for hak in range(0,6):
    tahmin=int(input("Tahmin et"))
    if tahmin==gizlisay:
        print("tebrikler")
        break
    elif tahmin<gizlisay:
         print("benim sayım daha büyük")
    else:
         print("benim sayım daha küçük")
else:
    print("sayıyı bulamadınız")

    

