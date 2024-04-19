with open("17.5_14652.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
for i in range(len(t)-1):
    if (t[i] > 0 and (round(t[i] ** 0.5) == (t[i] ** 0.5))) or (t[i + 1] > 0 and (round(t[i + 1] ** 0.5) == (t[i + 1] ** 0.5))):
        s = t[i] + t[i + 1]
        t1.append(s)
print(len(t1), max(t1))