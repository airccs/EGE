f = open("9.csv")
k = 0
for j in f:
    t = list(map(int, j.split(";")))
    p = []
    n = []
    for i in range(len(t)):
        if t.count(t[i]) == 2:
            p.append(t[i])
        if t.count(t[i]) == 1:
            n.append(t[i])
    if len(p) == 2 and len(n) == 5:
        n.sort()
        x = n[0] * n[1] * n[2]
        c = p[0] ** 2
        if x > c:
            k += 1
print(k)
#
f = open("92.csv")
k = 0

for j in f:
    t = list(map(int, j.split(";")))
    ch = 0
    nch = 0
    t1 = []
    for i in range(len(t)):
        if t[i] % 2 == 0:
            ch += 1
            t1.append(t[i])
        else:
            nch += 1
    if ch >= 1 and nch >= 1:
        if ch % 2 == 0 and nch % 2 == 1:
            m = max(t1)
            if m % 4 == 0:
                k += 1
print(k)