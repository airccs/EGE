"""for x in range(15545, 15844 + 1):
    delit = []
    for i in range(2, x):
        if x % i == 0:
            delit.append(i)
    if len(delit) == 5:
        print(x,max(delit))
"""
for x in range(950001, 100000 + 950001):
    F = 0
    delit = []
    for i in range(2, x):
        if x % i == 0:
            delit.append(i)
    if delit:
        F = max(delit) - min(delit)
        if F != 0 and F % 13 == 0:
            print(x, F)
