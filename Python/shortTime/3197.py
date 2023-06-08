# https://www.acmicpc.net/problem/3197 : 백조의 호수 (python3)
from collections import deque

# L 은 오리 .은 물 X 는 빙판


# 빙판을 녹이는 과정
def bfs(x, y):
    queue = deque()
    melt = []
    queue.append((x, y))
    visited[x][y] = True
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 > nx or nx >= r or 0 > ny or ny >= c:
                continue
            if lake[cx][cy] == "." and lake[nx][ny] == "X":
                melt.append((nx, ny))
            if not visited[nx][ny] and  lake[nx][ny] == ".":
                queue.append((nx, ny))
                visited[nx][ny] = True
    return melt


def melt(melt):
    for i in melt:
        lake[i[0]][i[1]] = "."


# 오리가 만나는지 확인
def swan(x, y):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True
    swan = []
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if 0 > nx or nx >= r or 0 > ny or ny >= c:
                continue
            if lake[nx][ny] == "L" and not visited[nx][ny]:
                swan.append((nx, ny))
            if not visited[nx][ny] and lake[nx][ny] == ".":
                queue.append((nx, ny))
            visited[nx][ny] = True
    return swan


# 호수의 크기를 입력받음
r, c = map(int, input().split())
lake = [list(input()) for _ in range(r)]
day = 0
# 호수의 크기만큼 방문 여부를 저장할 리스트 생성
while True:
    day += 1
    visited = [[False] * c for _ in range(r)]
    melted = bfs(0, 0)
    melt(melted)
    visited = [[False] * c for _ in range(r)]
    swanL = swan(0, 0)
    if len(swanL) == 2:
        break
print(day)
