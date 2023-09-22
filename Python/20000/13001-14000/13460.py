def move_red(x, y):
    return 0


n, m = map(int, input().split())
board = [[0] * n] * m
cnt = 0
for i in range(m):
    board[i] = list(input())
for i in range(11):
    for j in range(m):
        if board[i][j] == "R":
            red = [i, j]
        elif board[i][j] == "B":
            blue = [i, j]
        elif board[i][j] == "O":
            hole = [i, j]
"""
if red == hole:
        break
    if(cnt > 10):
        break
if cnt > 10:
    print(-1)
else:
    print(cnt)
"""
print(board)
