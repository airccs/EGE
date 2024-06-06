"""from itertools import *

k = 0
for i in permutations("ДОМИЩЕ", r=5):
    s = "".join(i)
    for sogl in "ДМЩ":
        s = s.replace(sogl, "Д")
    for gl in "ОИЕ":
        s = s.replace(gl, "О")
    if s[0] != "Д" and "ДД" not in s and "ОО" not in s:
        k += 1
        print(s, k)"""
"""from itertools import *
k = 0
for i in permutations("ДОМИЩЕ", r=5):
    s = "".join(i)
    for sogl in "ДМЩ":
        s = s.replace(sogl, "Д")
    for gl in "ОИЕ":
        s = s.replace(gl, "О")
    if s[0] != "Д" and "ДД" not in s and "ОО" not in s:
        k += 1
        print(s, k)"""
from itertools import *

k = 0
for i in set(permutations("ДИАНА", r=5)):
    s = "".join(i)
    k += 1
    print(s, k)
