for A in range(1000):
    bebra = True
    for x in range(1000):
        for y in range(1000):
            if not ((x >= 9) or ((2 * x) < y) or ((x * y) < A)):
                bebra = False
    if bebra:
        print(A)
        break
