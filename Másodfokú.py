import math

a = float(input('Kérem a másodfokú egyenlet főegyütthatóját: '))
while a==0:
    print('Ez ne lesz másodfokú egynelet')
    a = float(input('Kérem a konsatns tagot'))

b = float(input('Kérem a másodfokú egynelet főegyütthatóját: '))
c = float(input('Kérem a konstans tagot'))
d = b*b-4*a*c
print(d)
if d >= 0:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
    print('Van valós eredmény.')
else:
    x1 = (-b+math.sqrt(d))/(2*a)
    x2 = (-b-math.sqrt(d))/(2*a)
    print(x1)
    print(x2)
    print('Nincs valós eredmény.')