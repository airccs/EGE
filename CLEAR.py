s = "2006" * 298
while "200" in s or "666" in s:
    s = s.replace("200", "66", 1)
    s = s.replace("666", "66", 1)
print(s)
s = 300 * '5'
