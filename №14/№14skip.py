for x in "0123456789ABCDEF":
    if (int(f'D49{x}1', 16) + int(f'48A3{x}', 16)) % 14 == 0:
        print((int(f'D49{x}1', 18) + int(f'48A3{x}', 18)) // 14)