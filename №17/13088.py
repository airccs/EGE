with open("17_13088.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = 98817
for i in range(len(t) - 2):
    if (abs(t[i]) % 5 == 0) + (abs(t[i + 1]) % 5 == 0) + (abs(t[i + 2]) % 5 == 0) >= 1:
        if ((999 < t[i] < 10000) + (999 < t[i + 1] < 10000) + (999 < t[i + 2] < 10000)) == 2:
            s = t[i] + t[i + 1] + t[i + 2]
            if s > a:
                t1.append(s)
print(len(t1), max(t1))
