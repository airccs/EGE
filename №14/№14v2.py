s = 64 ** 2023 + 32 ** 2022 - 8 ** 2021 - 2
n = []
while s > 0:
    n.append(s % 20)
    s = s // 20
print(len(set(n)))
