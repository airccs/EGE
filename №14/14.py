# Значение арифметического выражения: 32**540 + 16**231 - 2**10 записали в системе счисления с основанием 2. Сколько цифр «1» содержится в этой записи?
s = 32 ** 540 + 16 ** 231 - 2 ** 10
s = bin(s)
print(s[2:].count('1'))

s = 32 ** 540 + 16 ** 231 - 2 ** 10
count = 0
while s > 0:
    if s % 2 == 1:
        count += 1
    s = s // 2
print(count)
