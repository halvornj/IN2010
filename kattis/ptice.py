import math
#brute force solution

N = int(input())
ans = input().strip()

A = "ABC"*math.ceil(N/3)
B="BABC"*math.ceil(N/4)
G="CCAABB"*math.ceil(N/6)
Asum = 0
Bsum=0
Gsum=0

for i in range(len(ans)):
    char = ans[i]
    if char == A[i]:Asum+=1
    if char == B[i]:Bsum+=1
    if char == G[i]:Gsum +=1

num = max(Asum, Bsum, Gsum)
print(num)
if Asum == num:print("Adrian")
if Bsum == num:print("Bruno")
if Gsum == num:print("Goran")