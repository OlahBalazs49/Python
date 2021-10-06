""""
név = input('Hogy tisztelhetem fényességedet?')
print('Üdvözöllek, nagyságos', név, '!', sep='')
stám1 = input('Melyik a legkedvesebb szívednek?')
szam1 = int(szam1) # típuskonverzió
szam2 = int(input('S melyik legyen a kedvenced a szamok vegtelen sokasagabol? '))
print('Eme két szám szorzata pediglen', szám1*szám2, 'lészen.')
"""
"""
#2
nev = input("mi a neved")
nap = imput("milyen nap van ma?")
print("Üdv ezen a szép' , nap,' -n, kedves ', név, sep= ")
"""
#3
autó = input('Egy autónév rendel! ')
végsebesség = int(input('Mennyivel megy a ' + autó + '? '))
ország = input('Hol készül a ' + autó + '? ')
mondat1 = ország + ' vidéken keresztül a ' + autó + ', ami' +str(végsebesség) + ' km/h végsebességre képes.'
print(mondat1)

mondat2 = '{} vidékein készül a {}, ami {} km/h végsebességre képes.'.format(ország, autó, végsebesség)
print(mondat2)

mondat3a = '{0} vidékein készül a {1}, ami {2} km/h végsebességre képes.'.format(ország, autó, végsebesség)
print(mondat3a)

mondat3b = '{0} vidékein készül a {2}, ami {1} km/h végsebességre képes.'.format(ország, végsebesség, autó)
print(mondat3b)

mondat4 = '{o} vidékein készül a {a}, ami {v} km/h végsebességre képes.'.format(o=ország, a=autó, v=végsebesség)
print(mondat4)

mondat5 = f'{ország} vidékein készül a {autó}, ami {végsebessség} km/h végsebességre képes.'
print(mondat5)
