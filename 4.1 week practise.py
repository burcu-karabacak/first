"""
liste1=[1,2,3,4,5]
liste2=liste1.copy()
liste1[0]=10
print(liste1,liste2)

# [10, 2, 3, 4, 5] [1, 2, 3, 4, 5]
      
liste1=[1,2,3,4,5]
liste2=liste1
liste1[0]=10
print(liste1,liste2)
# [10, 2, 3, 4, 5] [10, 2, 3, 4, 5]
"""
"""
cars=["bmw","mercedes","opel","mazda"]
print(cars)
print(len(cars))
print(cars[0],cars[-1])  # ilk ve son değerler
cars[3]="toyato"  # değeri değiştirme
print(cars)
print("mercedes" in cars) # elemanı mı?
print(cars[-2])
print(cars[0:3])
print(cars[:3])
print(cars[-2:]) # ['opel', 'toyato']
print(cars[-2:-5:-1]) # ['opel', 'mercedes', 'bmw']
"""
"""
cars=["bmw","mercedes","opel","mazda"] 
cars[-2:]= "toyato","renault" #son 2 elemenı T VE R olsun 
print(cars)  # YA DA cars[-1]="toyota"  cars[-2]="renault"
cars.append("audi")
cars.append("nissan")
print(cars)
del cars[-1]  # ya da cars.pop() son elemenı sildirme
print(cars)
cars.reverse() ## tersten yazdırma
print(cars)
### dir(list) tersten yazma
dir(list)
print(cars)
"""
"""
liste=["ağaç","yaprak","toprak","su","ateş"]
liste.clear()
print(liste)
"""
"""
liste=["ağaç","yaprak","toprak","su","ateş"]
liste.pop(2)
print(liste)
"""
"""
tek=[1,3,5,7]
cıft=[2,4,6,8]
tek.append(cıft)
print(tek) # [2,4,6,8] şeklinde ekliyor
print(len(tek)) 

tek.extend(cıft)
print(tek) # 2,4,6,8 şeklinde ekliyor  [1, 3, 5, 7, 2, 4, 6, 8]
tek.sort() # sıralandı [1, 2, 3, 4, 5, 6, 7, 8]
print(tek)
"""
"""
donanim = {“Türü”:”RAM”, “Tipi”:”DDR4”, “Kapasitesi”:”8 GB” }
donanim[“Hızı”]=”2400 MHz” #burada ekleme işlemi yapılmıştır.
print(donanim)

donanim = {“Türü”:”RAM”, “Tipi”:”DDR4”, “Kapasitesi”:”8 GB” }
donanim.pop(“Kapasitesi”) #burada silme işlemi yapılmıştır.
print(donanim)

donanim = {“Türü”:”RAM”, “Tipi”:”DDR4”, “Kapasitesi”:”8 GB” }
donanim2= {“Türü”:”Sabit Disk”, “Tipi”:”SSD”, “Kapasitesi”:”1 TB”}
donanimlarim={“donanim”:donanim, “donanim2”:donanim2}
print(donanimlarim)

"""
tup=('pyhon','C++','java')  # " tırnak farketmiyor
print(tup)
"""
a={1,2,3,4,5,5,5,5}
print(a) ## {1, 2, 3, 4, 5}
"""
#
dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
print(dersler[1])

#dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
#print(dersler(2)) ### eror indisler her durumda [ ]
dersler=("Python","C++ Dersleri","Java","C++ Dersleri")
dersler2=list(dersler)
dersler2[2]="C#"
print(dersler2)




