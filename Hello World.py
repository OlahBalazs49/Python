#eltávolítja a szóközöket az elejéről és a végéről
a = " Hello, World! "
print(a.strip())

#asd
a = "Hello, World!"
print(a.split(";"))

#konkatenció
a = "Hello"
b = "World"
c = a + b
print(c)
print(a+" " + b)

#szóköz hozzáadáshoz " " kell hozzáadni
a = "Hello"
b = "World"
c = a + b
print(c)

gyumolcs = "banán"
m = gyumolcs[-2]
print(m)

m = gyumolcs[0]
print(m)

#eredményül (index, karakter) értékpárokat kapunk
gyumlcs = "banán"
lista = list(enumerate(gyumolcs))
print(lista)

#az index operátor egy stringet ad vissza
#nincs külön típusú karakterek tárolására, ezek 1 hosszúságú stringek
primek = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
p4 = primek[4]
print(p4)

#hossz
gyumolcs = "banán"
hossz = len(gyumolcs)
print(hossz)

#utolsó betű
sz = len(gyumolcs)
utolso = gyumolcs[sz-1]
print(utolso)

#bejárás és a while
i = 0
while i < len(gyumolcs):
    karakter = gyumolcs[i]
    print(karakter)
    i += 1                    #i=i+1

#bejárás és a for

for c in gyumolcs:
    print(c)

elotag = "Törp"
utotagok_listaja = ["erős", "költő", "morgó", "öltö", "papa", "picur", "szakál" ]

for utotag in utotagok_listaja:
    print(elotag + utotag)

s = "A Karib-tenger kalózai"
print(s[0:1])       #A
print(s[2:14])      #Karib-tenger
print(s[15:22])     #kalózai

#a szeletelés, szemben az indexelő operátorral
#nem ad out of range hiba üzenetet ha túlmegyünk
gyumolcs = "banán"
gy = gyumolcs[:3]
print(gy)               #ban
gy = gyumolcs[3:]
print(gy)               #án
gy = gyumolcs[3:399]
print(gy)               #án

#keresünk egy szót
txt = "Hello, welcome to my world."
x = txt.find("welome")
y = txt.find("w")
print(x)

#a string format metódusa
#a format () segítségével illeszthat be a karakterláncokba:
""""
s1 = "A neve {0}!".format("Author")    #ezt csak úgy, erről nem volt szó!!!!
print(s1)
"""

nev = "Alice"
kor = 10
s2 "A nevem {1}, és {0} éves vagyok.".format(kor, nev)
print(s2)