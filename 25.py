from fnmatch import fnmatch

# 11??4*56

data = []
for x in range(0, 10**8, 211):
    if fnmatch(str(x), '11??4*56'):
        data.append([x, x // 211])
print(data)
