inp = list(map(int, input().strip().split()))
R,C,ZR, ZC = inp[0],inp[1],inp[2],inp[3]
matrix = []
for i in range(R):
    matrix.append(input().strip())
newMatrix = []
for row in matrix:
    newRow = ""
    for col in row:
        newRow += ZC*col
    for i  in range(ZR):
        newMatrix.append(newRow)

for row in newMatrix:
    print(row)
