# https://www.acmicpc.net/problem/3197 : 백조의 호수 (python3)
from collections import deque

# 1. 물과 백조의 위치를 각각 저장
# 2. 물과 접촉한 모든 빙판공간을 녹임
# 3. 백조가 서로 접촉할 수 있는지 확인
# 4. 반복
# 5. 백조가 접촉할 수 있게되면 프로그램을 종료하고 걸리는 날을 출력

# 너비우선탐색 알고리즘
# 1. 탐색 시작 노드를 큐에 삽입하고 방문처리
# 2. 큐에서 노드를 꺼내 해당 노드의 인접노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문처리
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복


def bfs(x, y, visited):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx, dy
            if nx < 0 or nx >= r or ny < 0 or ny >= c:
                continue
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))


# 호수 크기를 입력받고 물과 백조, 얼음의 위치를 받음
r, c = map(int, input().split())
lake = [list(input()) for _ in range(r)]

# 물과 백조의 위치를 각각 저장
water = []
swan = []
for i in range(r):
    for j in range(c):
        if lake[i][j] == ".":
            water.append((i, j))
        elif lake[i][j] == "L":
            swan.append((i, j))

# 물과 접촉한 모든 빙판공간을 녹임
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited = [[False] * c for _ in range(r)]
