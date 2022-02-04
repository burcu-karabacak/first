
"""
ogrenciNotlari={"Arzu":90,"Erdal":60,"Sumeyra":70,"Dua":90,"Meryem":100,"Yaren":90}
top=0
for i,j in ogrenciNotlari.items():
print("Öğrenci Adı: {0}\t Notu :{1}".format(i,j))
top+=jprint("Ortalama :{}".format(top/len(ogrenciNotlari)))
notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}
notlar["erdal"]["Mat"]
notlar["arzu"]["Eng"]


"""
"""
öntel={"Acil Çağrı Merkezi":"112","Polis İmdat":"155","Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
print(öntel.values())
print(dir(list))  
#öntel.pop("Acil Çağrı Merkezi")
#print(öntel)
"""
"""
öntel={"Acil Çağrı Merkezi":"112","Polis İmdat":"155","Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
if "Polis İmdat" in öntel:
    print("vardır")
else:
    print("Kullanıcı yoktur")

print(len("Polis İmdat "))
#öntel.clear()
#print(öntel)
if "Sağlık Bakanlığı İletişim Merkezi" in dict.keys(öntel): # dict.keys(öntel) sözlukteki anahtar kelime var mı diye sorduk
    print("var") #### dict(öntel) ledeki gibide olabilir
else:
    print("yok")
"""
"""
k={"python",'c',4,"cahit","python"}  # sözlüklerde dictionary index desteklemiyor
#print(len(k))
#print(dir(set)) # bunlar kullan. veri setlerini gösterir.
K=list(k)
print(K)
print(K[3])
print(K[0])
print(K[1])
print(K[2])

k=["python",'c',4,"cahit","python"] ##
print(len(k))
"""
"""
a=int(input("sayı giriniz"))
k={1,2,3,4,5}
k.add(a)
topla=0
for i in k:
    topla=topla+i
print(k)
print(topla)

"""
"""
#update
k1={1,2,3,4,5,6} # k1'e k2 yi ekledi
k2={7,8,9,10}
k1.update(k2)
print(k1)
k1.remove(4)
#k1.remove(11) # ******hata verir
print(k1) #keyeror[11]****
k1.discard(11) # discard la hata mesajı vermiyor****
print(k1)
"""


k1={1,2,3,4,5,6} # k1'e k2 yi ekledi
k2={7,8,9,10,6,5}
x={545,45,4554,98,26}
print(k1.union(k2))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(k1.union(k2.union(x)))#{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 4554, 26, 545, 98, 45}

