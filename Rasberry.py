forrásfájl = open('raspberries.txt','w', encoding = "utf-8")
rpk = []
for sor in forrásfájl:
    rpk.append(sor.strip().split(';'))
forrásfájl.close()

forrásfájl = open('raspberries.txt')
print(forrásfájl.read())
forrásfájl.close()