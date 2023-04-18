for n in range(3, 100):
    task = '3' + '5'*n

    while '25' in task or '355' in task or '555' in task:
        if '25' in task:
            task = task.replace('25', '32', 1)
        if '355' in task:
            task = task.replace('355', '25', 1)
        if '555' in task:
            task = task.replace('555', '3', 1)

    if sum([int(x) for x in task]) == 17:
        print(n)
        