import sys
import math
from heapq import heappush, heappop
def balance(A:list):
    if len(A) <= 0: return 
    if len(A) == 1:
        print(heappop(A))
        return
    splitIndex = math.floor(len(A)/2)
    a1 = [heappop(A) for a in range(splitIndex)]
    print(heappop(A))
    balance(a1)
    balance(A)




def main():
    inp = []    
    for i in sys.stdin:
        heappush(inp, int(i))
    balance(inp)
main()