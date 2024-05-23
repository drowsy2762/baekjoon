# https://www.acmicpc.net/problem/2933 : 미네랄 (python3)
from collections import deque
from sys import stdin

# 입력 최적화
input = stdin.readline

# 방향 벡터
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
turn = True


def destroy(y):
    global turn
    if turn == True:
        for i in range(c):
            if cave[r - y][i] == "x":
                cave[r - y][i] = "."
                turn = False
                return (y, i)
    else:
        for i in range(c - 1, -1, -1):
            if cave[r - y][i] == "x":
                cave[r - y][i] = "."
                turn = True
                return (y, i)


def findCluster(x, y):
    visited = [[False] * c for _ in range(r)]
    visited[x][y] = True
    q = deque([(x, y)])
    cluster = [(x, y)]
    while q:
        x, y = q[0]
        if len(q) > 0:  # 큐가 비어있는지 확인
            x, y = q.popleft()
        else:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (
                0 <= nx < r
                and 0 <= ny < c
                and not visited[nx][ny]
                and cave[nx][ny] == "x"
            ):
                visited[nx][ny] = True
                q.append((nx, ny))
    return cluster


def isFloating(cluster):
    for x, y in cluster:
        if x == r - 1 or cave[x + 1][y] == "x":
            return False
    return True


def applyGravity(cluster):
    minFallDistance = r
    for x, y in cluster:
        fallDistance = 0
        while x + fallDistance + 1 < r and cave[x + fallDistance + 1][y] == ".":
            fallDistance += 1
        minFallDistance = min(minFallDistance, fallDistance)

    for x, y in cluster:
        cave[x][y] = "."
        cave[x + minFallDistance][y] = "x"


def processTurn(height):
    hit = destroy(height)
    if hit:
        floatingClusters = []
        visited = [[False] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if cave[i][j] == "x" and not visited[i][j]:
                    cluster = findCluster(i, j)
                    if isFloating(cluster):
                        floatingClusters.append(cluster)
        for cluster in floatingClusters:
            applyGravity(cluster)


# 메인 함수
def solution():
    global cave, r, c
    r, c = map(int, input().split())
    cave = [list(input().strip()) for _ in range(r)]
    n = int(input())
    heights = list(map(int, input().split()))

    for height in heights:
        processTurn(height)

    for row in cave:
        print("".join(row))


solution()
