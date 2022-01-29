"""
sayi=list[1,3,5,7,9,12,19,21]
for i in sayi:
    if sayi%3==0:
        print(sayi)

toplam=0
for sayi i sayilar:
    toplam+=toplam
    print(sayi)

sayilar=[1,3,5,7,6,9,12,19,21]
for sayi in sayilar:
    if (sayi%2==0):
        sayi=sayi*sayi
        print("sayi kareleri",sayi)
       
sehir=['kocaeli','istanbul','ankara','izmir','rize']
for i in(sehir):
    if len(i)<=6:
        print(i)        

sehir=['kocaeli','istanbul','ankara','izmir','rize']
for i in(sehir):
    if len(i)<=6:
        pass
    print(i)

   
sehir=['kocaeli','istanbul','ankara','izmir','rize']
for i in range(len(sehir)):
    if len(sehir[i])<=5:
        print(sehir[i])

###kaç tane şehir var// 5 harf ya da daha az şehir
toplam=0
sehir=['kocaeli','istanbul','ankara','izmir','rize','hatay']
for i in sehir:
    if len(i)<=5:
        toplam=toplam+1
        print(i)
print("toplam şehir",toplam)

toplam=0
for i in range(1,10):
    if (i%2==1):
        print(i)
        toplam+=1
print("toplam:", toplam)        
"""
#n=[1,2,3,4,5,6,7,8,9,10]
"""
toplam=0
i=1
while i<=10:
    if i%2==1:
        toplam+=1
        print(i)
    i=i+1
print("toplam:", toplam)


for i in range(10,0,-2):
    print(i)
[10,0)
    
"""
"""
for i in range(1,20):
    if i%3==0:
        continue #uğramadan aşağı geç demek
    else:
        print(i)
"""
"""
for i in range(1,20):
    if i%3==0:
        print(i)    ### çıktı 1
2
3
3
4
5
6
6
7
8
9
9
10
11
12
12
13
14
15
15
16
17
18
18
19
    print(i)
"""
"""
for i in range(1,20):
    if i%3==0:
        break ## 3'e bölünmeyenleri sıralarken 1 2 de kalır
    print(i)    # girinti en başta olursa print 3 yazar çünkü en son 3 'te kalmıştı
print("merhaba")

"""
"""
i=1
while i<=10:
    print(i)
    i=i+1    #### girinti en başta ise sonsuz döngüü
print("merhaba")
"""
i=10
while i>=0:
    print(i)
    i=i-1    #### girinti en başta ise sonsuz döngüü
print("merhaba")






