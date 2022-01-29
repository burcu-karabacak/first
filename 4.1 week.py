
"""
tek_sayilar=[3, 5, 7, 9, 11, 13, 15, 17, 19]
print(tek_sayilar[::3])
print(tek_sayilar[0:6])
print(tek_sayilar[2:5])
print(tek_sayilar[:5])
print(tek_sayilar[3:])
print(tek_sayilar[0:8:2])
print(tek_sayilar[::8])

takim=["a","b","c"]
takim.append("ts")
print(takim)

takim=["a","b","c"]
takim.insert(2,"ts")
print(takim)

sebze=["lahana","marul","pırasa","ıspanak","fasulye"]
sebze.insert(2,"patlıcan")
print(sebze)

ilx1=["ankara","istanbul", "samsun"," k.maraş"]
ilx2=ilx1.copy()
print(ilx2)

takim=["GS","FB","BJK","TS","FB","FB"]
count=takim.count("FB")
say=takim.count("GS")
say1=takim.count("aa")
print(count,say,say1)
print(say)
print(say1)

s1=["adana","ankara","artvin","amasya","ağrı"]
s2=["burdur","balikesir","bursa"]
s1.extend(s2)
print(s1)
s1.sort()
print(s1)
"""      
sebze=["lahana","marul","pırasa","ıspanak","fasulye"]
iller=["sivas","samsun","sakarya","adana","anakara"]
print(sebze.index("ıspanak"))
print(iller.index("adana"))
print(iller.index("sivas"))
