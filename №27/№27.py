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