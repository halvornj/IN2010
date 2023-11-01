line = input().split()
N,P,S = line[0], line[1], line[2]
for i in range(int(S)):
    nums = input().split()
    if P in nums[1:]: print("KEEP")
    else:print("REMOVE")