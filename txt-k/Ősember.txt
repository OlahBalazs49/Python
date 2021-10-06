név = input("Ősemeber név mi?")
print(név)
bogyók = int(input)('Hány bogyód van? '))

if bogyók < 10:
    minősítés = 'zsenge'
elif bogyók > 20:
    minősítés = 'nagy koponya'
else:
    minősítés = 'gyüjtögető'

print(f'{név} egy {minősítés}.')