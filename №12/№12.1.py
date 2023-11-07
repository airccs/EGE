for n in range(3, 10000):
    s = '0' + '6' * n
    while '06' in s or '566' in s or '666' in s:
        if '06' in s:
            s = s.replace('06', '6', 1)
        if '566' in s:
            s = s.replace('566', '60', 1)
        if '666' in s:
            s = s.replace('666', '5', 1)
    summ = s.count('5') * 5 + s.count('6') * 6
    print(summ)
