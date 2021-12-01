import random

szam1 = int(input("Kérek egy számot!"))
while szam2%2 == 1:
    szam2 = random.randrange(10 , 50)
    
SZAM3 = 5
#halmaz
szamok = {23}
szamok2.add(szam1)
szamok2.add(szam2)
szamok2.add(SZAM3)
print(szamok2)
#lista
szamok = []
szamok.append(szam1)
szamok.append(szam2)
szamok.append(SZAM3)
if szam1 %2 == 0:
    print("Páros")
else:
    print("Páratlan")
print(szam1, szam2)
szam4 = str(szam1)
wr = open("balazs.txt","w")
wr.write(nev)
wr.write("\n szam4")
wr.close()

lista = [1,2,3,4,5,"abc","def"]
with open("balazs.txt", "w") as file:
    for item in lista:
        file.write("%s\n" % item)

gyumolcsok = ["eper","barack","ananász"]
print(f' a gyumolcsok lista a következőket tartalmazza:{gyumolcsok}')
for (i,y) in enumerate (gyumolcsok):
    print(i,y)

print("",.join)