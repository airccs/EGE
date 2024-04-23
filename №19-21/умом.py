from functools import lru_cache


def moves(s):
    return s + 2, s + 3, 2 * s # все возможные ходы


@lru_cache
def game(s):
    if any(m >= 88 for m in moves(s)): return "win1"  # если хоть 1 больше,то позиция выигрышная
    # if any(game(m) == "win1" for m in moves(s)): return "neud" (неудачный ход)
    if all(game(m) == "win1" for m in moves(s)): return "loss1"  # проигрышная поз
    if any(game(m) == "loss1" for m in moves(s)): return "win2"  # выигрыш вторым
    if all(game(m) == "win1" or "win2" for m in moves(s)): return "loss12"  #


for s in range(1, 88):
    if game(s) == "loss12":
        print(s)