P = int(input().strip())

for i in range(P):
    line = list(map(int, input().strip().split()))
    #line = [int(x)for x in input().strip().split()]
    K = line[0]
    N = line[1]
    out = f"{K} "
    s1 = int(((N+1)*N)/2)
    s2 = sum([x for x in range(1, 2*N, 2)])
    s3 = sum([x for x in range(2, 2*N+1, 2)])
    
    out = f"{K} {s1} {s2} {s3}"
    print(out)