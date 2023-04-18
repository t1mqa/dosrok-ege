for n in range(4, 15):

    nbinary = bin(n)[2:]
    if n % 3 == 0:
        result = nbinary + nbinary[-3:]
    else:
        ostatok = n % 3 * 3
        binaryOstatok = bin(ostatok)[2:]
        result = nbinary + binaryOstatok
    R = int(result, 2)

    print(n, R)
