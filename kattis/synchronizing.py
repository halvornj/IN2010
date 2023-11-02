n = int(input().strip())

while n!= 0:
    l1 = []
    l2 = []
    for i in range(n):
        l1.append(int(input().strip()))
    for i in range(n):
        l2.append(int(input().strip()))
    l1sorted = l1.copy()
    l1sorted.sort()
    l2sorted = l2.copy()
    l2sorted.sort()
    l2ordered = []
    for i in range(len(l1)):
        l2ordered.append(l2sorted[l1sorted.index(l1[i])])
    for num in l2ordered:
        print(num)
    print()
    n=int(input().strip())