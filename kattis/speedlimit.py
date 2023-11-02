S = int(input().strip())
while S != -1:
    out = ""
    dist = 0
    elapsed = 0
    for j in range(S):
        line = list(map(int, input().strip().split()))
        dist += line[0]*(line[1]-elapsed)
        elapsed=line[1]
    print(f"{dist} miles")
    S = int(input().strip())
