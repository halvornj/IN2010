line = input().split()
N,Q = int(line[0]), int(line[1])

companies = [None]*(100_000)
initialPositions = list(map(int, input().split()))
for i in range(len(initialPositions)):
    ls = []
    ls.append(i+1)
    companies[initialPositions[i]+1] = ls

for i in range(Q):
    query = list(map(int, input().split()))
    #*move company
    if query[0]==1:
        oldCompLs = [ls for ls in companies if ls is not None and query[1] in ls]
        oldCompLs[0].remove(query[1])
        if companies[query[2]] is None:
            ls = []
            ls.append(query[1])
            companies[query[2]] = ls
            continue
        else:
            companies[query[2]].append[query[1]]
    
    #*print distance
    else: 
        startI = None
        stopI = None
        for i in range(len(companies)):
            el = companies[i]
            if el is None:continue
            if query[1] in el: startI = i
            if query[2] in el: stopI = i
            if (startI is not None) and (stopI is not None):break
        
        assert type(startI) == int
        assert type(stopI) == int
        print(abs(stopI-startI))
