N = int(input())

count = 0

for i in range(N):
    line = input().lower().replace(" ","")
    if "pink" in line or "rose"in line:
        count+=1

if count>0: print(count)
else: print("I must watch Star Wars with my daughter")