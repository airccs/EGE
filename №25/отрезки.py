for x in range(123456, 123487+1):
    delit = []
    for i in range(1,x+1):
        if x % i ==0:
            delit.append(i)
    if len(delit)==6:
        print(delit)
"""
cnt=0
for x in range(800001, 100000 + 800001):
    for i in range(111, x,100):
        if x % i == 0:
            print(x,i)
            cnt+=1
            break
    if cnt==5:
        break
"""