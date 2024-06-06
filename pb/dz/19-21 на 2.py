from functools import lru_cache


def moves(x, s):
    return [[min(x, s) + i, max(x, s)] for i in range(1, min(x, s) + 1)]


@lru_cache(None)
def game(x, s):
    if any(sum(m) >= 63 for m in moves(x, s)): return "win1"
    if all(game(*m) == "win1" for m in moves(x, s)): return "loss1"
    if any(game(*m) == "loss1" for m in moves(x, s)): return "win2"
    if all(game(*m) == "win1" or game(*m) == "win2" for m in moves(x, s)): return "loss12"


x = 7
for s in range(1, 56):
    if game(x, s) == "loss12":
        print(s)
