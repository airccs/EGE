for n in range(101, 200):
    s = '1' * n
    while '111' in s:
        s = s.replace('111', '2', 1)
        s = s.replace('222', '1', 1)
    if s == '11':
        print(n)
        break
