from functools import lru_cache


def moves(x, s):
    return (x + 2, s), (x * 2, s), (x, s + 2), (x, s * 2)


@lru_cache
def game(x, s):
    if any(sum(m) >= 73 for m in moves(x, s)): return "win1"  # если хоть 1 больше,то позиция выигрышная
    if all(game(*m) == "win1" for m in moves(x, s)): return "loss1"  # или game(m[0],m[1])
    if any(game(*m) == "loss1" for m in moves(x, s)): return "win2"
    if all(game(*m) == "win1" or game(*m) == "win2" for m in moves(x, s)): return "loss12"


x = 4
for s in range(1, 69):
    if game(x, s) == "loss12":
        print(s)
