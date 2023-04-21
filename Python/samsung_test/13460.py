n, m = map(int, input().split())
board = [[0] * n] * m
for i in range(m):
    board[i] = list(input())
for i in range(n):
    for j in range(m):
        if board[i][j] == "R":
            red = [i, j]
        elif board[i][j] == "B":
            blue = [i, j]
        elif board[i][j] == "O":
            hole = [i, j]
    if red == hole:
        break
print(board)
