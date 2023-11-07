for x in range(0, 10):
    if (int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) % 11 == 0:
        print(x, (int('1234' + str(x), 15) + int('5' + str(x) + '678', 15)) // 11)
