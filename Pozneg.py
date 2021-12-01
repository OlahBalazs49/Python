def pozneg(szám):
    if szám < 0:
        print(szám, 'Pozitív.')
    elif szám < 0:
        print(szám, 'Negatív.')
    else:
        print('A szám nulla.')

szám = None
while szám !='':
    szám = input('Írj ide egy számot!')
    if szám !='':
        szám = float(szám)
        pozneg(szám)