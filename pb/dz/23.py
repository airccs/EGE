def f(x, y, k):
    if x > y:
        return 0
    if x == y and k.count("*") == 2:
        return 1
    return f(x + 2, y, k + "+") + f(x + 3, y, k + "+") + f(x * 2, y, k + "*") + f(x * 3, y, k + "*")
print(f(1, 51, ""))
