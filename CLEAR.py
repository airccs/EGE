"""def tos(x):
    st = ""
    while x > 0:
        st += str(x % 4)
        x = x // 4
    return st[::-1]
print(tos(6))
"""


def f(x, y):
    return (x < a) and (y < a) and (x * y > 601)
for a in range(1, 1000):
    if all(f(x, y) == 0 for x in range(1, 1000) for y in range(1, 1000)):
        print(a)
