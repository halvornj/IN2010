import math
N = int(input())
M = int(input())

remainder = M%N
for i in range(N):
    out = math.floor(M/N)*"*"
    if remainder>0:
        out+="*"
        remainder-=1
    print(out)