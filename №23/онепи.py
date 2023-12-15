def f(start, end):
    if start == end:
        return 1
    if start > end or start == 11:
        return 0
    return f(start + 1, end) + f(start * 2, end) + f(start ** 2, end)


print(f(2, 15) * f(15, 20))
