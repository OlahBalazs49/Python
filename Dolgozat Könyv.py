nev = input('Mi a neve?')
ev = int(input('Hány éves?'))
if ev > 3:
    könyv = 'Totyogóknak a kettes számrenszerről'
if ev > 6:
    könyv = 'Hackeljük meg az óvodát'
if ev > 14:
    könyv = 'Felhőtechnológia a menzán'
if ev > 18:
    könyv = 'Big data a középiskolában'

print(f'{nev} a {könyv}.')