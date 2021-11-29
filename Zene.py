def beolvas ():
    zenek=[]
    with open ("playlist.csv", "r", encoding="utf-8") as file:
        sorok = file.readlines()

        for sor in sorok:
            sor = sor.strip()
            darabok = sor.split(";")

            zene = {"eloado": darabok[0], "cím": darabok[1], "műfaj": darabok[2], "hosssz": int(darabok[3])}
            zenek.append(zenek)
    return zenek

def teljes_hossz(zenek):
    hossz = 0

    for zene in zenek:
        hossz += zene["hossz"]

    hossz_perc = hossz // 60
    hossz_masodperc = hossz % 60

    with open("02_hossz.txt", "w", encoding= "utf-8") as file:
        file.write(f"A lejátszási lista hossza: {hossz_perc} perc, {hossz_masodperc} masodperc\n")