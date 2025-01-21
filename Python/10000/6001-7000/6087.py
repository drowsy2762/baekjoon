# https://www.acmicpc.net/problem/6087 : 레이저 통신 (python3)
from sys import stdin
from collections import deque

input = stdin.readline

w, h = map(int, input().split())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
grid = []
c = []

for i in range(h):
    row = list(input().rstrip())
    grid.append(row)
    for j in range(w):
        if row[j] == "C":
            c.append((i, j))


visited = [[-1] * w for _ in range(h)]


def bfs(start):
    q = deque()
    q.append((start[0], start[1], -1, 0))
    visited[start[0]][start[1]] = 0

    while q:
        x, y, direction, mirrors = q.popleft()
        print(visited[2])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "*":
                new_mirrors = mirrors
                if direction != -1 and direction != i:
                    new_mirrors += 1

                if visited[nx][ny] == -1 or visited[nx][ny] >= new_mirrors:
                    visited[nx][ny] = new_mirrors
                    q.append((nx, ny, i, new_mirrors))


bfs(c[0])

print(visited[c[1][0]][c[1][1]])
