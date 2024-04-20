"""with open("task_17 (1).txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
dl = 17989
summ = 905289730
sr = summ // dl
for i in range(len(t) - 1):
    if (t[i] > sr) + (t[i + 1] > sr) == 1:
        if (str(t[i]).count("11")) + (str(t[i]).count("11")) >= 1:
            mod = abs(t[i]- t[i+1])
            t1.append(mod)
print(len(t1),max(t1))"""
"""with open("17.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = 99413
for i in range(len(t)-2):
    if (int(len(str(abs(t[i]))) == 5) + int(len(str(abs(t[i + 1]))) == 5) + int(len(str(abs(t[i + 2]))) == 5)) == 2:
        s = t[i]+t[i+1]+t[i+2]
        if s <= a:
            t1.append(s)
print(len(t1),max(t1))"""

"""with open("17.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = -78600
for i in range(len(t)-2):
    m = ((len(str(abs(t[i]))) == 5)+(len(str(abs(t[i+1]))) == 5)+(len(str(abs(t[i+2]))) == 5))
    if m <= 2:
        s = t[i] + t[i+1] + t[i+2]
        if s >= a:
            t1.append(s)
print(len(t1),min(t1))"""

with open("17.txt") as f:
    st = f.read()
t = list(map(int, st.split()))
t1 = []
a = 9911
for i in range(len(t)-1):
    if (oct(t[i])[-1]) == (oct(t[i] + 1)[-1]):
        if (t[i] % 35 != 0 and t[i + 1] % 35 != 0) and ((t[i] % 5 == 0 and t[i + 1] % 7 == 0) or (t[i + 1] % 5 == 0 and t[i + 1] % 7 == 0)):
            s = t[i] ** 2 + t[i + 1] ** 2
            if s <= a**2:
                t1.append(t[i] + t[i + 1])
print(len(t1), min[t1])
