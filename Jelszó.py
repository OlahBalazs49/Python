#JELSZO = input('Mi a a jelszava?')
#print(JELSZO)
JELSZO = 'jelszo'
jelszo = None
while jelszo != JELSZO:
    jelszo = input('Mi a a jelszava?')
    if jelszo != JELSZO:
        print('nem jó')
        pass
print('ügyes vagy')