P = list(range(16, 60))
Q = list(range(27, 72))
A = []
for x in range(1, 100):
    if ((not(x in A))<=((x in P)<=(not(x in Q)))) == False:
        A.append(x)
print(A)
#max - min = otvet