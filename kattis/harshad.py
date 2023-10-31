num = int(input())

ans = None

while ans is None:
    nums = [int(x) for x in str(num)]
    if (num % sum(nums))==0:ans = num
    else:num +=1
print(ans)