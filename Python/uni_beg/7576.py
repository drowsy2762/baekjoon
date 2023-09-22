# https://www.acmicpc.net/problem/7576 : 토마토(python3)
from sys import stdin
from collections import deque

input = stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    cnt = 0
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= m and nx <= 0 and ny >= n and ny <= 0:
                continue
            if graph[nx][ny] == 0:
                q.append((nx, ny))
                graph[nx][ny] = 1
        cnt += 1


m, n = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]
dist = []
bfs(0, 0)
print(graph)
