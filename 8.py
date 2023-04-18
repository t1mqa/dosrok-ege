from itertools import product

p = product("АКЛМНЯ", repeat=5)

for x, num in zip(p, range(1, 8000)):
    word = ''.join(x)
    if word[0:2] == 'КМ':
        print(word, num)
        break
