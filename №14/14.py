# Значение арифметического выражения: 32**540 + 16**231 - 2**10 записали в системе счисления с основанием 2.
# Сколько цифр «1» содержится в этой записи?

s = 32**540 + 16**231 - 2**10
s = bin(s)
print(s[2:].count('1'))

# Значение арифметического выражения: 34321 + 4914 + 7 записали в системе счисления с основанием 7.
# Сколько цифр «0» содержится в этой записи?

s = 343 ** 21 + 49 ** 14 + 7
count = 0
while s > 0:
    # вместо 0 то число которое нужно посчитать
    # вместо 7 то основание сс
    if s % 7 == 0:
        count += 1
    s = s // 7
print(count)
