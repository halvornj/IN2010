set = set()
N = int(input())

for i in range(N):
    line = input().strip().split()
    isAnomaly = ""
    postfix = ""
    if line[0]=="entry":
        if line[1] in set:
            isAnomaly=" (ANOMALY)"
        set.add(line[1])
        postfix = " entered"
    else:
        if line[1] not in set:
            isAnomaly=" (ANOMALY)"
        else:
            set.remove(line[1])
        postfix = " exited"
    print(line[1] +postfix+isAnomaly)