import sys
import math
def balance(A:list)->list:
    if(len(A)) <= 1:return A
    splitIndex = math.floor(len(A)/2)
    return [A[splitIndex]]+balance(A[:splitIndex])+balance(A[splitIndex+1:])

def main():
    inp = []    
    for i in sys.stdin:
        inp.append(int(i))
    out = balance(inp)
    for i in out:
        print(i)
main()