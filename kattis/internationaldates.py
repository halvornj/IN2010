def solve(date):
    if int(date[0]) >12: return"EU"
    if int(date[1])> 12:return "US"
    return"either"

date = input().split("/")[:-1]

print(solve(date))
