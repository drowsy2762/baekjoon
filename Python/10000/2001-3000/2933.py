# https://www.acmicpc.net/problem/2933 : 미네랄 (python3)
from collections import deque
from sys import stdin

# 미네랄 캐진거 확인하고 클러스터 떨어지는거 확인
# 떨어지는거 확인하고 떨어지는거 떨어지게 하기

# input runtime 최적화
input = stdin.readline

# 입력값을 모두 입력받음
r, c = map(int, input().split())
cave = [list(input()) for _ in range(r)]
n = int(input())
height = list(map(int, input().split()))

# 미리 필요한 부분을 전역함수로 선언
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[False] * c for _ in range(r)]


def clearVisited():
    visited = [[False] * c for _ in range(r)]


def throwStick(y):
    nx = 0
    while 1:
        if cave[nx][y] == "x":
            cave[nx][y] == "."
        nx += 1
    checkGravity(y)


def checkCluster():
    x, y = 0, 0
    mq = deque()
    while cq:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if cave[nx][ny] == "x":
                mq.append(nx, ny)
            cq.append(nx, ny)


def checkGravity(y):
    for x in range(0, r - 1):
        if cave[x][y] == "x":
            cave[x][y] = "."
            mq = deque()
            visited2 = [[False] * c for _ in range(r)]
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if cave[nx][ny] == "x" and not visited2[nx][ny]:
                    mq.append(nx, ny)
            break
