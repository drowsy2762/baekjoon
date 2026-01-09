# https://www.acmicpc.net/problem/6087 : 레이저 통신 (python3)
# 2025-10-23
from sys import stdin
from collections import deque

input = stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

w, h = map(int,input().split())
graphs = [list(input().rstrip()) for _ in range(h)]

# 방향이 바뀔때마다 거울을 추가한다고 봐야함
# 2안 벽 혹은 구조물에 접촉할때까지 일자로 직진함
# 3안 방향을 관리함 visited 리스트를 3차원으로 설계한후 방향을 관리함 
def bfs(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
 