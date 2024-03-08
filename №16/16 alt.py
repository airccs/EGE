f = [0] * 10000
for n in range(10000):
    if n == 1:
        f[n] = 1
    if n == 2:
        f[n] = 2
    if n > 2:
        f[n] = (n - 1) * (n - 2) + f[n - 1] + f[n - 2]
print(f[2021] - f[2019] - 2 * f[2018] - f[2017])