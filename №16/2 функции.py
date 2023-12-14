def F(n):
    if n == 2:
        return 1
    if n > 2:
        return 3 * F(n - 1) + 4 * G(n - 1) - n * 2 + 4


def G(n):
    if n == 2:
        return 1
    if n > 2:
        return 4 * F(n - 1) + 3 * G(n - 1) + 6


print(F(8) + G(8))
