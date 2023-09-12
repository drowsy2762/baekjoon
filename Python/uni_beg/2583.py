# https://www.acmicpc.net/problem/2583 : python3(영역 구하기)
from sys import stdin

input = stdin.readline

m, n, k = map(int, input().split())

graph = [[0] * n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    queue = []

    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y
        if graph[nx][ny] == 0:
            queue.append([nx, ny])


for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    if lx > rx:
        tem = rx
        rx = lx
        lx = tem
    if ly > ry:
        tem = ry
        ry = ly
        ly = tem
    for j in range(ly, ry):
        for k in range(lx, rx):
            graph[j][k] = 1

print(graph)
