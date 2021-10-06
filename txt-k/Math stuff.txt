import math, cmath

a= input('Kérek egy másodfokú egyenlet főegyüthatóját: ')
a= float(a)
while a ==0:
    print('Ez nem lesz másodfokú egyenlet, nem oldom meg.')
    a= input('Kérek egy másodfokú egyenlet főegyüthatóját: ')
    a= float(a)

b= input('Kérek egy másodfokú egyenlet főegyüthatóját: ')
c= input('Kérem a diszkrimináns tagot: ')
print('A diszkrimináns tagot: ')
b= float(b)
c= float(c)

d= b*b-4*a*c

#d= math.pow(b,2)-4*a*c
print('A diszkrimináns értéke', d)

if d>=0:
    print=('Van valós megoldás.')
    x1= (-b-math.sqrt(d))/(2*a)
    x2= (-b+math.sqrt(d))/(2*a)
    print('Az egyik megoldás', x1)
    print('Másik megoldás', x2)
else:
    print ('Nincs valós megoldás')
    x1= (-b-cmath.sqrt(d))/(2*a)
    x2= (-b+cmath.sqrt(d))/(2*a)
    print('Az egyik megoldás', x1)
    print('Másik megoldás', x2)