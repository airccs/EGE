f = open('17')
a = []
for s in f:
    a.append(int(s))
sum = []
for i in range(len(a) - 1):
    if (a[i] > 0 and a[i] ** (1/2) % 1 == 0) or (a[i + 1] > 0 and a[i] ** (1/2) % 1 == 0):
        sum.append(a[i] + a[i + 1])
print(len(sum), min(sum))

'''f = open('17.66.txt')
a = []
for s in f:
    a.append(int(s))
sum = []
for i in range(len(a) - 1):
    if a[i] > 850 or a[i + 1] > 850:
        sum.append(a[i] ** 2 + a[i + 1] ** 2)
print(len(sum), max(sum))'''
