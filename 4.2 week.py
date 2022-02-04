#a
"""
list=["B","İ","L","İ","Ş","İ","M",]
list.sort()
print(list)
#b

list=["B","İ","L","İ","Ş","İ","M",]
list.reverse()
print(list)

#c

list=["B","İ","L","İ","Ş","İ","M",]
print(list.count("İ"))

#ç

list=["B","İ","L","İ","Ş","İ","M",]
del list[4:6]
print(list)
#
ders=["b","i","l","i","ş","i","m"]
ders.remove("ş")
ders.pop(4)
print(ders)
#d

list=["B","İ","L","İ","Ş","İ","M",]
a=list.copy()
print(a)

#e silme clear

#f
list=["B","İ","L","İ","Ş","İ","M",]
print(list.index("L"))

"""
#1
"""
a=[35,26,81,64]
a.sort()
print(a)
 
#2
a=[35,26,81,64]
a.reverse()
print(a)

#3
a=[35,26,81,64]
print(a.count(26))

#4
a=[35,26,81,64]
a.remove(81)
print(a)

#5 tüm elemanları sil
#numbers=[35,26,84,64]liste1=[1.4,6.8]liste1 =numbers.extend(liste1)print(numbers)

meyve=["elma","armut"]
aliste=["peynir","süt",meyve]
print(len(aliste))  
print(aliste)      #['peynir', 'süt', ['elma', 'armut']]

for i in aliste:
    print(i)
"""
"""
bellekler=["RAM", "ROM"]
ekran_kartlari=["Paylaşımlı", "Paylaşımsız"]
sabit_diskler=["SSD"]
birimler=bellekler, ekran_kartlari, sabit_diskler   #(['RAM', 'ROM'], ['Paylaşımlı', 'Paylaşımsız'], ['SSD'])
print(birimler)

bellekler=["RAM", "ROM"]
ekran_kartlari=["Paylaşımlı", "Paylaşımsız"] # ['RAM', 'ROM', 'Paylaşımlı', 'Paylaşımsız', 'SSD']
sabit_diskler=["SSD"]
birimler=bellekler+ ekran_kartlari+ sabit_diskler
print(birimler)


sozluk = {"Bilim insanı":"Aziz Sancar", "Şair":"Mehmet Akif Ersoy", "Astronom":"Ali Kuşçu" }
meslek=sozluk.copy()
print(meslek)


sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
print(sozluk.values())
print(sozluk.keys())

sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
del sozluk
print(sozluk)  #not defined uyarısı verir.



sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
sozluk.clear()
print(sozluk)  #not defined uyarısı verir.

sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
sozluk["Matematikçi"]="Cahit ARİF"
print(sozluk)


sozluk={"Bilim İnsanı":"Aziz SANCAR","Şair":"Mehmet Akif ERSOY","Astronom":"Ali Kuşçu"}
print("sanatçı" in sozluk)
print(sozluk)
sozluk["Bilim İnsanı"]="Canan Dağdeviren" # anahtar kelime yoksa yeni ekliyor varsa güncelliyor
print(sozluk)
print(sozluk["Şair"])

"""
notlar={"Erdal":"83","Arzu":"88","Yaren":"48"}
a=(input("isminizi girin"))
b=int(input(" notuzu girin"))
print(notlar["Erdal"])
notlar[a]=b
print(notlar)
#####
ogrenciNotlari={"Arzu":90,"Erdal":60,"Sumeyra":70,"Dua":90,"Meryem":100,"Yaren":90}
top=0
for i,j in ogrenciNotlari.items():
print("Öğrenci Adı: {0}\t Notu :{1}".format(i,j))
top+=j
print("Ortalama :{}".format(top/len(ogrenciNotlari)))

notlar={"erdal":{"Mat":45,"Eng":78,"Phys":78,"Science":77},"arzu":{"Mat":45,"Eng":78,"Phys":78,"Science":77}}

