egyik = int(input("Adjon meg egy számot"))
masik = int(input("Adjon meg egy maásik számot"))
jel = input("Adjon meg egy műveleti jelet")

#print('A művelet eredménye:', end ='' )

print('A művelet eredménye:', end ='' )
if jel == '+':
        print(egyik+masik)
elif jel == '-':
    print(egyik-masik)
elif jel == '%':
    print(egyik % masik)
elif jel == '/':
    print(egyik / masik)
elif jel == '>>':
    print(egyik >> masik)