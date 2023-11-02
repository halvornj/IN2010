import math

#park in floor(avg) of stores
#sum abs(store - position)

N = int(input().strip())
for i in range(N):
    num = int(input().strip())
    positions = list(map(int, input().strip().split()))
    avg = math.floor(sum(positions)/len(positions))

    dist = 0
    dist += (max(positions)-avg)*2
    dist+=abs(min(positions)-avg)*2
    print(dist)