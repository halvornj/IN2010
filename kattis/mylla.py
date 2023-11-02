def find_winner(board):
#tired, just brute-force
    if board[0]=="OOO":return "Jebb"
    if board[1]=="OOO":return "Jebb"
    if board[2]=="OOO":return "Jebb"
    if board[0][0]=="O" and board[1][0]=="O"and board[2][0]=="O":return"Jebb"
    if board[0][1]=="O" and board[1][1]=="O"and board[2][1]=="O":return"Jebb"
    if board[0][2]=="O" and board[1][2]=="O"and board[2][2]=="O":return"Jebb"
    if board[0][0]=="O" and board[1][1]=="O"and board [2][2]=="O":return"Jebb"
    if board[0][2]=="O"and board[1][1]=="O"and board[2][0]=="O":return"Jebb"
    return "Neibb"


board = []
board.append(input().strip())
board.append(input().strip())
board.append(input().strip())
print(find_winner(board))
