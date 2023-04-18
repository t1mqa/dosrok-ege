with open('9file.txt', 'r') as taskFile:
    lines = [x.strip() for x in taskFile.readlines()]
    lines = [[int(x) for x in x.split('\t')] for x in lines]
    k = 0
    for line in lines:
        if len(set(line)) == 5:
            maxnum = max(line)
            minnum = min(line)
            if 2 * (max(line) + min(line)) >= sum([x for x in line if x != maxnum and x != minnum]):
                k += 1

    print(k)