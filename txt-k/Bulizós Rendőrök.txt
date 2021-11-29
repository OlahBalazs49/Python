bulizok_szama = int(input("A házibuliban résztvevők száma: "))
rendorok_szama = int(input("A rendőrök száma: "))
print()

if rendorok_szama == 0:
    print("Minden bulizó megmenekült!")
else:
    elkapottak_szama = 0

    for i in range(1, rendorok_szama + 1):
        elkapottak_szama += i

    if elkapottak_szama < bulizok_szama:
        elmenekultek_szama = bulizok_szama - elkapottak_szama
        print(elkapottak_szama, "bulizót elkaptak," , elmenekultek_szama)
    else:
        print("Ajaj, mindekit elkaptak!")