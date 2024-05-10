B = list(range(24, 91))
C = list(range(47,116))
A = []
for x in range(1, 1000):
    if ((x in C)<=((not(x in A)and(x in B))<=(not(x in C)))) == False:
        A.append(x)
print(A)
#max - min = otvet
print(90-47)