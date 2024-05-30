# https://www.acmicpc.net/problem/9376 : 탈옥 (Python3)
from sys import stdin
from collections import deque

input = stdin.readline
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs():
    visited = [[False] * w for _ in range(h)]
    money = [[0] * w for _ in range(h)]
    q = deque()
    for i in range(h):
        for j in range(w):
            if jail[i][j] == "$":
                q.append((i, j, 0))
                visited[i][j] = True

    while q:
        x, y, c = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                visited[nx][ny] = True
                if jail[nx][ny] == "*":
                    continue
                if jail[nx][ny] == "#":
                    q.append((nx, ny, c + 1))
                    money[nx][ny] = c + 1
                else:
                    q.appendleft((nx, ny, c))
                    money[nx][ny] = c

    result = 1e9
    for i in range(h):
        for j in range(w):
            if jail[i][j] == "#":
                result = min(result, money[i][j])
    for i in range(h):
        print(money[i])
    return result


def jail_break():
    global jail, w, h
    h, w = map(int, input().split())
    jail = [list(input().rstrip()) for _ in range(h)]
    result = bfs()
    print(result)


def solution():
    n = int(input())
    for _ in range(n):
        jail_break()


solution()
