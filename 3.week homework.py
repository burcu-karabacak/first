#1 1-100 Arası Sayıları Ekranda Listeleyen Python kodunu yazınız
"""
i=1
while i<100:
    print(i)
    i=i+1
"""
    
#2 1-100 arası Çift Sayıları Listeleyen Python kodunu yazınız
"""
i=1
while i<100:
    if i%2==0:
        print(i)
    i=i+1
"""
# 3 1-100 Arası Tek Sayıları Listeleyen Python Örneği
"""
i=1
while i<100:
    if i%2==1:
        print(i)
    i=i+1
"""
#4 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bulan Python kodunu yazınız.
"""
i=1
while i<100:
    if i%3==0 or i%5==0:
        print(i)
    i+=1
"""        
#5  1 den başlayıp kullanıcının girdiği sayıya kadar listeleyen
"""
i=1
a=int(input("enter your num"))
while i<=a:
    print(i)
    i+=1
"""
#6 Girilen metnin harflerini alt alta yazdıran Python kodunu yazınız
"""
name=input(" Enter your name")
for i in str(name):
    print(i)
print("adını heceledim")    
"""
#7 Girilen 2 sayı aralarındaki sayıları toplamı
"""
sum=0
a=int(input(" Enter your number1"))
b=int(input(" Enter your number2"))
for i in range(a+1,b):
    sum=sum+int(i)
print(sum)
"""
#8 ASAL MI?
a=int(input(" Enter your number1"))
i=1
while i<=a:
    if i
