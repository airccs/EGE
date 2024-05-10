P = list(range(16, 85))
Q = list(range(27,44))
A = (list(range(1000)))
for x in range(1, 1000):
    if (((x in A) <= (x in P)) or (x in Q)) == False:
        A.remove(x)
print(A)
#max - min = otvet
print(84-16)