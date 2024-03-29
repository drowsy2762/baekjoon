# https://www.acmicpc.net/problem/2589 : 보물섬(python3)
from sys import stdin
from collections import deque

input = stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0] * m for _ in range(n)]
    visited[x][y] = 1
    cnt = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= n or nx < 0 or ny >= m or ny < 0:
                continue
            if graph[nx][ny] == "L" and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y] + 1
                cnt = max(cnt, visited[nx][ny])
                q.append((nx, ny))
    return cnt - 1


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

result = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == "L":
            result = max(result, bfs(i, j))

print(result)
