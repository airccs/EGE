s = 6056
n = []
while s > 0:
    n.append(s % 12)
    s = s // 12
print(n.count(3))
