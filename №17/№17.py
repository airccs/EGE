f = open('17')
a = []
for s in f:
    a.append(int(s))
sum = []
for i in range(len(a) - 1):
    if (a[i] > 0 and a[i] ** (1/2) % 1 == 0) or (a[i + 1] > 0 and a[i] ** (1/2) % 1 == 0):
        sum.append(a[i] + a[i + 1])
print(len(sum), min(sum))

'''f = open('17.8.txt')
a = [int(s) for s in f]
sum = []
min9 = min([x for x in a if abs(x) % 10 == 9])
for i in range(len(a) - 1):
    if (str(a[i])[-1] == str(a[i + 1])[-1] and
            ((a[i] % 9 == 0) + (a[i + 1] % 9 == 0) == 1) and
            (a[i]** 2 + a[i+1] ** 2) <= min9 ** 2):
        sum.append(a[i] ** 2 + a[i + 1] ** 2)
print(len(sum), max(sum))


f = open('17.txt')
a = [int(s) for s in f]
chet = [x for x in a if x % 2 == 0]
sr_ar = sum(chet) / len(chet)
sum = []
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) or (a[i + 1] % 3 == 0)) and ((a[i] < sr_ar) or (a[i + 1] < sr_ar)):
        sum.append(a[i] + a[i + 1])
print(len(sum),max(sum))
'''
