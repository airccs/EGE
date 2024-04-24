from functools import lru_cache


def moves(x, s):
    return (x + 4, s), (x * 3, s), (x, s + 4), (x, s * 3)


@lru_cache
def game(x, s):
    if any(sum(m) >= 105 for m in moves(x, s)): return "win1"  # если хоть 1 больше,то позиция выигрышная (ход 1 челикса)
    # if any(game(*m) == "win1" for m in moves(x,s)): return "neud" #(неудачный ход)
    if all(game(*m) == "win1" for m in moves(x, s)): return "loss1"  # или game(m[0],m[1])
    if any(game(*m) == "loss1" for m in moves(x, s)): return "win2"
    if all(game(*m) == "win1" or game(*m) == "win2" for m in moves(x, s)): return "loss12"


x = 4
for s in range(1, 101):
    if game(x, s) == "neud":
        print(s)

