s = open("../24.3.txt").readline()
a = s.split("R")
print(len(max(a, key=len)))

'''
s = open("24.3.txt").readline()
a = s.split("O")
t = [a[i] + "O" + a[i + 1] for i in range(len(a) - 1)]
print(len(max(t, key=len)))

s = open("24.4.txt").readline()
s = s.replace("S", "T")
s = s.replace("R", "T")
s = s.replace("A", "U")
for i in range(1000):
    if "UT" * i in s:
        print(i)
        
s = open("24.txt").readline()
s = s.replace("XZZY", "XZZ ZZY")
s = s.split()
print(len(max(s, key=len)))
'''
