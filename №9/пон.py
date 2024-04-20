f = open("")
cnt = 0
for s in f:
    t = list(map(int, s.split()))
    povt = [x for x in t if t.count(x) > 1]
    nep = [x for x in t if t.count(x) == 1]
    if len(povt) == 2 and povt[0] % 2 == 0 and
