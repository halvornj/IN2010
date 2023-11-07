inp = input().strip().split()
n, T = int(inp[0]), int(inp[1])
line = list(map(int, input().strip().split()))

count = 0
for num in line:
    T -= num
    if T >=0:
        count+=1
    else:break

print(count)