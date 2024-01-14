P = list(range(3, 19))
Q = list(range(11, 25))
A = []
for x in range(1, 100):
    if (((x in P) and (x in Q)) <= (x in A)) == False:
        A.append(x)
print(A)
#max - min = otvet