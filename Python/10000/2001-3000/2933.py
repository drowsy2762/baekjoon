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


# 미네랄을 파괴하는 함수
def destroy(y, direction):
    if direction == True:
        for i in range(c):
            if cave[y - 1][i] == "x":
                cave[y - 1][i] = "."
                direction = False
                cluster = cluster(y - 1, i)
    else:
        for i in range(0, c, -1):
            if cave[y - 1][i] == "x":
                cave[y - 1][i] = "."
                direction = True
                cluster = cluster(y - 1, i)


# 떨어진 클러스터의 구성을 확인하는 함수
def cluster(x, y):
    visited = [[0] * c for _ in range(r)]
    visited[x][y] = 1
    q = [(x, y)]
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if visited[nx][ny] == 0 and cave[nx][ny] == "x":
                visited[nx][ny] = 1
                q.append((nx, ny))
    return visited


def solution():
    n = int(input())
    height = list(map(int, input().split()))
    direction = False

    for i in range(r):
        print("".join(cave[i]))


solution()
