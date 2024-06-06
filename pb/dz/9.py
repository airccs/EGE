f = open("9.18.txt")
k = 0
for s in f:
    a = list(map(int, s.split()))
    a.sort()
    if a[0] + a[1] == a[2]:
        k += 1
print(k)
