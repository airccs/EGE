import sys
sys.setrecursionlimit(6200)
def F(n):
    if n <= 6:
        return n
    if n > 6:
        return 2 * n + 3 + F(n - 1)
print(F(6188) - F(6185))

from functools import lru_cache
import sys
sys.setrecursionlimit(6200)
@lru_cache()
def F(n):
    if n <= 6:
        return n
    if n > 6:
        return 2 * n + 3 + F(n - 1)
print(F(6188) - F(6185))