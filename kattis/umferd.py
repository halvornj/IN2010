emptyCount = 0
total = 0

m = int(input().strip())
n = int(input().strip())

for i in range(n):
    line = input().strip()
    total +=len(line)
    emptyCount += line.count(".")

print(float(emptyCount)/float(total))