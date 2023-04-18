with open('17task.txt', 'r') as taskFile:
    lines = [x.strip() for x in taskFile.readlines()]
    print(lines)
    k = 0
    maxsum = 0
    maxDvuznach = 0
    for x in [int(x) for x in lines]:
        if len(str(x)) == 2:
            if x > maxDvuznach:
                maxDvuznach = x
    for num, nextNum in zip(lines, lines[1:]):
        if (len(num) == 2 and len(nextNum) != 2) or (len(nextNum) == 2 and len(num) != 2):
            num, nextNum = int(num), int(nextNum)
            if sum([num, nextNum]) % maxDvuznach == 0:
                k += 1
                if sum([num, nextNum]) > maxsum:
                    maxsum = sum([num, nextNum])
    print(k, maxsum)

