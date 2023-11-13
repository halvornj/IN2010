n = int(input())
vol = 7

for i in range(n):
    if input().strip()=="Skru op!":
        vol = min(vol+1, 10)
    else:
        vol = max(vol-1, 0)

print(vol)