"""
metin=["python"]
diziharfler=list(metin)
print(diziharfler)
list(metin)
"""
"""
d1=[1,2,3]
d2=[4.0,5.7,4.5]
d3=["a","b","c"]
dizi=[d1,d2,d3]
dizi=["elam","armut","portakal"]
cikti=dizi[2]
print(cikti)
"""
"""
dizi=["a","b","c","d","e","f","g","h"]
a=dizi[len(dizi)-1]
print(a)
a=dizi[5:]
print(a)

dizi=["a","b","c","d"]
a=dizi+["e"]
print(a)

dizi1=["a","b","c","d"]
dizi1[4]=["k"]
a=dizi1
print(a)

dizi1=["a","b","c","d"]

cikti=dizi1+["z"]

cikti[4]="w"

print(cikti)

dizi=["a","b"]
dizi.append("c")
dizi.append("c") #yine ekler listede ama KÜME DE (ADD)1 KERE EKLER
#dizi=dizi*10
print(dizi)
kume={1,2,3,4}
kume.add(5)
kume.add(5)
print(kume)   # kümede eleman tekrarı yok
"""
"""
dizi=["a","b","a","b","a","c",]
say=dizi.count("a")
print(say)

dizi=["a","b","c"]
dizi.insert(1,"x")    #1.indise x eklnedi a x b c
print(dizi)

a=" Habitat-python   "
print(a.strip())

b=" ankara; kayseri,nevşehir,kırşehir,iç anadolu bölgesi"
print(b.split("a"))

"""
a="Ankara,Edirne,Malatya,Bolu,Bursa,İzmir"


b=a.replace(",","-")

print(b)

metin="bugünlerde 'outliners' kitabını okuyorum"
print(metin)




print(" \" Cümle başında ve sonunda tırnak var \"  ")








