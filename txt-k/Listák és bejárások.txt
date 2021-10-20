import random
honap = ["január", "február", "március",\
     "április", "május"]
for i in honap:
    print(i, end="")
print("\nA tömb mérete: ", len(honap))
for j in range(len(honap)):
    print("%d. honap: %s" % (j+1, honap[j]))
print(random.choice(honap))