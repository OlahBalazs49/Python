gyumolcs = {"alma", "körte", "banán" }
kosar = {}
gyumolcs.clear(kosar)
gyumolcs.copy(kosar)
print(gyumolcs)


zoldseg = {"répa", "karfiol", "brokkoli"}
hus = {"sertés", "marha", "csirke"}
zoldseg.difference(hus)
zoldseg.difference_update(hus)
zoldseg.intersection(hus)
zoldseg.intersection_update(hus)
print(zoldseg.isdisjoint(hus))

hus.difference(zoldseg)
hus.difference_update(zoldseg)
hus.intersection(zoldseg)
hus.intersection_update(zoldseg)
print(hus.isdisjoint(zoldseg))
print(zoldseg)
print(hus)


csokolade = {"Snickers", "Bounty", "Milkyway"}
csokolade2 = {"Milka", "Boci", "Tibi"}
csokolade.intersection(csokolade2)
csokolade.intersection_update(csokolade2)
csokolade2.intersection(csokolade)
csokolade2.intersection_update(csokolade)
csokolade2.symmetric_difference(csokolade)
print(csokolade)
print(csokolade2)


#issubset
x = {"A", "B", "C"}
y = {"D", "E", "F", "G", "H", "I"}

z = x.issubset(y)

print(z)

#issuperset
x = {"a", "b", "c"}
y = {"d", "e", "f", "g", "h" ,"i"}

z = x.issuperset(y)
print(z)

#symmetric_difference
x = {"1", "2", "3"}
y = {"4", "5", "6", "7", "8", "9"}

z = x.symmetric_difference(y)

print(z)

#union
x = {"foci", "kosar", "rop"}
y = {"vizi", "tennis", "golf"}

z = x.union(y)

print(z)

#discard
browser = {"chrome", "firefox", "edge"}

browser.discard("edge")

print(browser)

#pop
sport = ['uszas', 'kezi', 'pingpong']

sport.pop(1)