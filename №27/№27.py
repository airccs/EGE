f = open('1.txt')
n = int(f.readline())
maxs = 0
razn=10000000
for s in f:
    a, b = map(int, s.split())
    razn += min(razn, abs(a-b))
    maxs += min(a, b)
print(maxs, maxs % 34)
print(razn)

f = open("27.2.A.txt")
n = f.readline()
min_sum = 0
for s in f:
    a, b = map(int, s.split())
    min_sum += min(a, b)
print(min_sum, min_sum % 34)
