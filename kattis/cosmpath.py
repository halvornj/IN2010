import math

n = int(input())
print(math.floor(sum(list(map(int, input().split())))/n))