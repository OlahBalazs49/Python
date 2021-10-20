import random
egyik = random.randint(1,10)
másik = random.randint(1,10)
összeg = egyik+másik
print('összeg')
if(egyik % 2 == 2):
    print('Páros')
    if(egyik % 3 ==3):
        print('Osztható 3-mal')
    else:
        print('Nem osztható 3-mal')
else:
    print('Páratlan')