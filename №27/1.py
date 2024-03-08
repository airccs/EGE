f = open("27.1.B.txt")
n = f.readline()
max_sum = 0
min_razn = 100000
for s in f:
    a, b = map(int, s.split())
    if abs(a - b) != 0:
        min_razn = min(min_razn, abs(a - b))
    max_sum += max(a, b)
print(max_sum, max_sum % 6)
print(min_razn + max_sum)
