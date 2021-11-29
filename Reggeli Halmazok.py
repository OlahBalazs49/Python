reggeli = {'vaj', 'tea', 'Pirítos'}
reggeli.add('víz')
#reggeli.remove('körte')
reggeli.discard('körte')
print(reggeli)

ebed = {}
#ebed = set['halaszlé', 'kenyér', True ]

print(type( ebed ))
print( ebed )

print( reggeli & ebed )
print( reggeli | ebed )
print( reggeli - ebed )
print( reggeli ^ ebed )

gyumolcskosar = ['eper', 'alma', 'szilvia', 'eper']
fajta = set()
for gyumolcs in gyumolcskosar:
    fajta.add(gyumolcs)
print(fajta)


    # egy elem hozzáadása
    reggeli.add('lekvár')

    # egy nem meghatározott elem eltávolítása
    reggeli.pop()
    
    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, akkor hibát eredményez
    reggeli.remove('sajt')

    # egy bizonyos elem eltávolítása
    # ha nincs ilyen elem, nem eredményez hibát
    reggeli.discard('sajt')
    
  
    reggeli = {'víz', 'tea', 'vaj', 'pirítós'}
    ebed = {'víz', 'halászlé', 'kenyér'}

    # metszet
    print(reggeli & ebed)
    # unio
    print(reggeli | ebed)
    # különbség
    print(reggeli - ebed)
    # csak az egyikben, vagy csak a másikban
    print(reggeli ^ ebed)