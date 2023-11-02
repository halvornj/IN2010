N = int(input())
names = input().strip().split()
print(names[12%len(names)])