"""s = 6542 ** 324 - 3560 ** 67 + 730 ** 12 - 510
k = 0
while s > 0:
    if s % 3 == 2:
        k += 1
    s = s // 3
print(k)
"""
for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:14]:
    for y in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:14]:
        a = int(f"ABCD3{y}2{x}1", 14)
        b = int(f"192{x}9", 14)
        s = a + b
        if s % 107 == 0:
            print(x, s // 107)
