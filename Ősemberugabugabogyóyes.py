név = input("Ősemeber név mi?")
print(név)

bogyók = int(input)('Bogyó hány?'))

if bogyók < 10:
    minősítés = 'maga egy balfék!'
elif bogyók > 20:
    minősítés = 'maga nagyon ügyes volt!'
else:
    minősítés = 'gyüjtögető'

print(f'{név}, egy {minősítés}.')