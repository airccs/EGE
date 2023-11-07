s = '>' + 24 * '7' + 15 * '5' + 11 * '3'
while ">7" in s or ">5" in s or ">3" in s:
    if ">7" in s:
        s = s.replace('>7', '555>', 1)
    if ">5" in s:
        s = s.replace('>5', '5>', 1)
    if ">3" in s:
        s = s.replace('>3', '7>', 1)
print(s.count('5') * 5 + s.count('7') * 7 + s.count('3') * 3)
