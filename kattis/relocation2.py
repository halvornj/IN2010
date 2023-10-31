line = input().split()
N,Q = int(line[0]), int(line[1])

locations = {}


initialPositions = list(map(int, input().split()))

for i in range(len(initialPositions)):
    locations[i+1]=initialPositions[i]


for i in range(Q):
    query = list(map(int, input().split()))
    #*move company
    if query[0]==1:
        locations[query[1]] = query[2]
    else:
        print(abs(locations[query[2]]-locations[query[1]]))