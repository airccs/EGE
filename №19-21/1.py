def f(s, m):
    if s >= 56:
        return m % 2 == 0
    if m == 0:
        return 0
    t = [f(s + 1, m - 1), f(s * 3, m - 1)]
    return any(t) if (m - 1) % 2 == 0 else all(t)  # Если в 19 номере "после неудачного хода",то all меняем на any


print("19", [s for s in range(1, 56) if not f(s, 1) and f(s, 2)])
print("20", [s for s in range(1, 56) if not f(s, 1) and f(s, 3)])
print("21", [s for s in range(1, 56) if not f(s, 2) and f(s, 4)])
