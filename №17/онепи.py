with open("17_12106.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = 468
for i in range(len(t) - 1):
    if ((t[i] < 0) + (t[i + 1] < 0)) == 1:
        s = t[i] + t[i + 1]
        if s % a == 0:
            s2 = t[i] ** 2 + t[i + 1] ** 2
            t1.append(s2)
print(len(t1), min(t1))
