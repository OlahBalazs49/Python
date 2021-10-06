OLVADÁSI_PONT = 1539
FORRÁS_PONT = 2750
hőfok = int(input("Hőfok:"))
if hőfok < OLVADÁSI_PONT:
    print("szilárd") 
elif hőfok < FORRÁS_PONT:
    print("folékony")
else:
    print("gáz")
    