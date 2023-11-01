nums = list(map(int, input().split()))
wc, hc, ws, hs = nums[0],nums[1],nums[2],nums[3]
print(int((ws < wc-1)and (hs<hc-1)))