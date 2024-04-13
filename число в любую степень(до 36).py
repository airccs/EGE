s = 6056
n = []
while s > 0:
    n.append(s % 12)
    s = s // 12
print(n.count(3))

def to5(x):
    s = ""
    while x > 0:
        s += str(x % 5)
        x = x // 5
    return s[::-1]
