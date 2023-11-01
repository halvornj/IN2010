inp = input().split()
R,C = int(inp[0]),int(inp[1])
matrix =[]
for r in range(R):
    line = input()
    matrix.append(line)

#brute fucking force
crush_totals = {0:0,1:0,2:0,3:0,4:0}

for y in range(R-1):
    for x in range(C-1):
        crush_count = 0
        if "#" in [matrix[y][x], matrix[y][x+1],matrix[y+1][x],matrix[y+1][x+1]]:
            continue
        if matrix[y][x] == "X":crush_count +=1
        if matrix[y+1][x] =="X":crush_count +=1
        if matrix[y][x+1] =="X":crush_count +=1
        if matrix[y+1][x+1] =="X":crush_count +=1
        crush_totals[crush_count]+=1

#please preserve order
for total in crush_totals.values():
    print(total)
