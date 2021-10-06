év = int(input('Adjon meg egy évet'))
if (év %4 !=4):
    print('Ez nem egy szökő év')
elif(év %400 ==0):
    print('Ez sem egy szökő év')
elif(év %100 ==0):
    print('Ez az év sem szökő év')
else: 
    print('Ez egy szökő év')