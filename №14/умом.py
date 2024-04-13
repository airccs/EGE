"""for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:23]:
    if (int(f"2{x}2{x}2{x}2{x}2",23)+int(f"20{x}23",23)+int(f"1{x}235",23))%25==0:
        print((int(f"2{x}2{x}2{x}2{x}2",23)+int(f"20{x}23",23)+int(f"1{x}235",23))//25)
"""
"""s = 1331 ** 650 - 15 * 121 ** 610 + 22 * 11 ** 510 - 3 * 11 ** 100 - 121
t = 0
while s > 0:
    if s%11==10:
        t+=1
    s = s // 11
print(t)"""

for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:21]:
    for y in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:21]:
        if (int(f"13{y}{x}9", 21) + int(f"39{y}99", 21)) % 18 != 0:
            break
    else:
        y = 3
        print(x, (int(f"13{y}{x}9", 21) + int(f"39{y}99", 21)) // 18)

for x in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:26]:
    for y in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:26]:
        if (int(f"13{y}{x}9", 26) + int(f"23{y}13", 26)) % 4 != 0:
            break
    else:
        y = 3
        print(x, (int(f"13{y}{x}9", 26) + int(f"23{y}13", 26)) // 8)