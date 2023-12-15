def f(s1, s2, m):
    if s1 + s2 >= 342:
        return m % 2 == 0
    if m == 0:
        return 0
    t = [f(s1 + 2, s2, m - 1), f(s1 * 5, s2, m - 1), f(s1, s2 + 2, m - 1), f(s1, s2 * 5, m - 1)]
    return any(t) if (m - 1) % 2 == 0 else all(t)  # Если в 19 номере "после неудачного хода",то all меняем на any


print("19", [s2 for s2 in range(1, 342) if f(11, s2, 2)])
print("20", [s2 for s2 in range(1, 342) if not f(11, s2, 1) and f(11, s2, 3)])
print("21", [s2 for s2 in range(1, 342) if not f(11, s2, 2) and f(11, s2, 4)])
