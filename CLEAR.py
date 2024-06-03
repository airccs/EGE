b = list(range(24, 91))
c = list(range(47, 116))
a = []
for x in range(0, 1000):
    if ((x in c) <= ((not (x in a) and (x in b)) <= (not (x in c)))) == False:
        a.append(x)
print(a)
