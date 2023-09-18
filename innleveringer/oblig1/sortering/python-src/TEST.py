from merge import sort
from countswaps import CountSwaps

tester = [2,5,4,3,6,91,3,55,98,58,34,22]
tester = CountSwaps(tester)

print(tester)
print(f"swaps before sort: {tester.swaps}")
tester = sort(tester)
print(tester)
print(f"swaps after sort: {tester.swaps}")