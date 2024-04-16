# https://www.acmicpc.net/problem/2933 : 미네랄 (python3)
from collections import deque
from sys import stdin

# 미네랄 캐진거 확인하고 클러스터 떨어지는거 확인
# 떨어지는거 확인하고 떨어지는거 떨어지게 하기

# input runtime 최적화
input = stdin.readline

# 미리 필요한 부분을 전역함수로 선언
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
r, c = map(int, input().split())
cave = [list(input().rstrip()) for _ in range(r)]


def destroy(y, direction):
    if direction == True:
        for i in range(c):
            if cave[y - 1][i] == "x":
                cave[y - 1][i] = "."
                direction = False
                cluster = cluster(y - 1, i, cave)
    else:
        for i in range(0, c, -1):
            if cave[y - 1][i] == "x":
                cave[y - 1][i] = "."
                direction = True
                cluster = cluster(y - 1, i, cave)


def cluster(x, y):
    visited = [[0] * c for _ in range(r)]
    visited[x][y] = 1
    q = [(x, y)]
    cluster = []
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 0 and cave[nx][ny] == "x":
                cluster.append((nx, ny))
                visited[nx][ny] = 1
                q.append((nx, ny))


def gravity(cluster):
    if not cluster:
        return
    while True:
        for x, y in cluster:
            if x == r - 1 or cave[x + 1][y] == "x":
                return
        for i in range(len(cluster)):
            cluster[i] = (cluster[i][0] + 1, cluster[i][1])


def solution():
    n = int(input())
    height = list(map(int, input().split()))
    direction = False
    for i in height:
        destroy(i, direction)
        # cluster(cave)

    for i in range(r):
        print("".join(cave))


solution()
