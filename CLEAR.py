from functools import lru_cache
def moves(s):
    t = [s+1]
    if s % 2 !=0:
        t.append(s*2)
    if s % 2 ==0:
        t.append(s*1.5)
    return t

@lru_cache
def game(s):
    if any(m >= 84 for m in moves(s)): return "p1"
    if all(game(m) == "p1" for m in moves(s)): return "v1"
    if any(game(m) == "v1" for m in moves(s)): return "p2"
    if all(game(m) == "p1" or game(m) == "p2" for m in moves(s)): return "v12"

for s in range(1, 84):
    if game(s) == "v12":
        print(s)
