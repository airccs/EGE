def tr(n, m, k):
    return max(n, m, k) < sum([n, m, k]) - max(n, m, k)


def f(x):
    return not ((tr(x, 11, 18) == (not (max(x, 5) > 68))) and tr(x, a, 5))


for a in range(1, 300):
    if all(f(x) == 1 for x in range(1, 3000)):
        print(a)
