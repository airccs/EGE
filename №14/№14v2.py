# Найдите количество уникальных цифр в двадцатеричной записи числа 7777290 - 77729 + 772 - 7.

s = 7777 ** 290 - 777 ** 29 + 77 ** 2 - 7
n = []
while s > 0:
    n.append(s % 20)
    s = s // 20
print(len(set(n)))

'''2 вариант'''

s = 7777 ** 290 - 777 ** 29 + 77 ** 2 - 7
a = set()
while s > 0:
    a.add(s % 20)
    s //= 20
print(len(a))
