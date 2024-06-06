"""import sys
sys.setrecursionlimit(3000)
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return n + 2+ F(n - 1)
print(F(2028) + F(2022))"""
f = [0]*3000
for n in range(1,2300):
    if n == 1:
        f[n] = 1
    if n > 1:
        f[n] = (2 * n - 2) * f[n - 1]
print(f[2012] / f[2010])