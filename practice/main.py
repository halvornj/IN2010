import MergeSort as mrg
import random as r
testArray = []
for i in range(100):
    testArray.append(r.random())


mySorted = mrg.sort(testArray)
defSort = testArray.copy()
defSort.sort()

assert mySorted == defSort
