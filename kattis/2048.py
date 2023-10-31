line2 = input().split()
line3 = input().split()
line4 = input().split()


move = input()
x = 0
y = 0
#parse integers
for i in range(line1):
    line1[i] = int(line1[i])
    line2[i] = int(line2[i])
    line3[i] = int(line3[i])
    line4[i] = int(line4[i])
    
board = [line1, line2, line3, line4]

if move =="0":
    #go left
    for i in range(3,0, -1):
        for j in range(4):
            while board[imaginarypointer][j] != 0 or board[imaginarypointer-1][j]
                if (board[i-1][j] == board[i][j]):
                    board[i-1][j] +=board[i][j]
                    board[i][j] = 0
                else:
                    board[i-1][j] = board[i][j]
                    board[i][j] = 0
elif move =="1":
    #go up
    for 

elif move =="2":
    #go right
    

elif move =="3":
    #go down
