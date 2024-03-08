"""def f(x, y, k):
    if x - 1 > y:
        return 0
    if x == y:
        return 1
    if k == "-":
        return f(x * 2, y, "*") + f(x * 3, y, "*")
    return f(x - 1, y, "-") + f(x * 2, y, "*") + f(x * 3, y, "*")


print(f(3, 16, ""))
"""

"""
def f(x, y, k):
    if x > y or "***" in k or "+++" in k:
        return 0
    if x == y:
        return 1
    return f(x + 1, y, k + "+") + f(x * 2, y, k + "*")


print(f(1,20,""))
"""


def f(x, y, k):
    if x - 1 > y or "***" in k or "--" in k:
        return 0
    if x == y:
        return 1
    return f(x - 1, y, k + "-") + f(x * 2, y, k + "*") + f(x * 3, y, k + "*")
print(f(3,120,""))