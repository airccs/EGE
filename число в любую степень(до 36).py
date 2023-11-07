s = 200 ** 3333 - 100 ** 2222 + 50 ** 1111 - 11
n = []
while s > 0:
    n.append(s % 3)
    s = s // 3
print(n.count(2))
