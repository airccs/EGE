from functools import lru_cache


def moves(s):
    return s + 4,s * 2


@lru_cache(None)
def game(s):
    if any(m >= 155 for m in moves(s)): return "win1"
    if all(game(m) == "win1" for m in moves(s)): return "loss1"
    if any(game(m) == "loss1" for m in moves(s)): return "win2"
    if all(game(m) == "win1" or game(m) == "win2" for m in moves(s)): return "loss12"

for s in range(1, 141):
    if game(s) == "loss12":
        print(s)
