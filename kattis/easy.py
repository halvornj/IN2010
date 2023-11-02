N = int(input().strip())
while N != 0:
    sumN = sum([int(x)for x in str(N)])
    coeff = 11
    sumProduct = sum([int(x) for x in str(N*coeff)])
    while sumProduct != sumN:
        coeff+=1
        sumProduct = sum([int(x) for x in str(N*coeff)])

    print(coeff)

    N = int(input().strip())