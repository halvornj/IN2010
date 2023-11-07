kitten = input().strip()
#parent[x] = y, y is parent of x
parents = {}
path = ""
line = ""
while "-1" not in line:
    line = input().split()
    for i in range(1, len(line)):
        parents[line[i]] = line[0]

while kitten is not None:
    path+=kitten+ " "
    kitten = parents.get(kitten, None)

#fjerner siste whitespace
path = path[:-1]
print(path)