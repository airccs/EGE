with open("17.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = 9911
for i in range(len(t)-1):
    if (oct(t[i])[-1]) == (oct(t[i+1])[-1]):
        if (t[i] % 5 == 0 and t[i + 1] % 7 == 0 and t[i] % 35 != 0 and t[i + 1] % 35 != 0) or (t[i + 1] % 5 == 0 and t[i] % 7 == 0 and t[i] % 35 != 0 and t[i + 1] % 35 != 0):
            s = t[i] ** 2 + t[i + 1] ** 2
            if s <= a**2:
                t1.append(t[i] + t[i + 1])
