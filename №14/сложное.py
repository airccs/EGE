'''# В выражении 32x437 + 5x2937 x обозначает некоторую цифру из алфавита системы счисления с основанием 37.
# Определите наименьшее значение x, при котором значение данного выражения кратно 63.
# Для найденного x вычислите частное от деления данного выражения на 63 и запишите его в ответе в десятичной системе счисления.'''
for x in range(0, 37):
    if ((3 * 37 ** 3 + 2 * 37 ** 2 + x * 37 ** 1 + 4 * 37 ** 0) + (
            5 * 37 ** 3 + x * 37 ** 2 + 2 * 37 ** 1 + 9 * 37 ** 0)) % 63 == 0:
        print(((3 * 37 ** 3 + 2 * 37 ** 2 + x * 37 ** 1 + 4 * 37 ** 0) + (
                5 * 37 ** 3 + x * 37 ** 2 + 2 * 37 ** 1 + 9 * 37 ** 0)) // 63)

for x in range(0, 14):
    s = (3 * 14 ** 3 + 2 * 14 ** 2 + x * 14 ** 1 + 4 * 14 ** 0) + (
            5 * 14 ** 3 + x * 14 ** 2 + 2 * 14 ** 1 + 9 * 14 ** 0)
    if s % 107 == 0:
        print(s // 107)

'''#В выражении ABCD3y2x114 + 192x914 переменные х и у обозначают некоторые цифры из алфавита системы счисления с основанием 14. 
# Определите наименьший х, для которого есть такой y, при котором значение данного выражения кратно 107. 
# При найденных значениях х и y определите частное от деления выражения на 107 и укажите его в ответе в десятичной системе счисления.'''

for x in "0123456789ABCD":
    for y in "0123456789ABCD":
        s = (int(f'ABCD3{y}2{x}1', 14) + int(f'192{x}9', 14))
        if s % 107 == 0:
            print(x, y, s // 107)

'''# В системе счисления с основанием p выполняется равенство 1xy1p + xyx9p = D65yp. 
# Буквами x и y обозначены некоторые цифры из алфавита системы счисления с основанием p. 
# Определите значение числа xxyp и запишите это значение в десятичной системе счисления.'''
for p in range(14, 37):
    for x in range(0, p):
        for y in range(0, p):
            if (1 * p ** 3 + x * p ** 2 + y * p ** 1 + 1 * p ** 0) + (
                    x * p ** 3 + y * p ** 2 + x * p ** 1 + 9 * p ** 0) == (
                    13 * p ** 3 + 6 * p ** 2 + 5 * p ** 1 + y * p ** 0):
                print(x * p ** 2 + x * p ** 1 + y * p ** 0)
