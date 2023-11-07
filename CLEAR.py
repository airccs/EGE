for x in "0123456789ABCDEFGH":
    if (int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)) % 17 == 0:
        print((int(f'AB5{x}3', 18) + int(f'EF{x}13', 18)) // 17)