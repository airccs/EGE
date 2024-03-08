f = open("27.2.A.txt")
n = f.readline()
min_sum = 0
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
print(min_sum, min_sum % 34)
