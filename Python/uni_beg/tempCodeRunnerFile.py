# https://www.acmicpc.net/problem/2606 : 바이러스 (python3)
from sys import stdin

input = stdin.readline

n = int(input())
t = int(input())
cnt = 1

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]


def dfs(node):
    if visited[node] == False:
        visited[node] = True
        global cnt
        cnt += 1
        for i in graph[node]:
            if visited[i] == True:
                continue
            return dfs(i)
        return 0
    else:
        return 0


for _ in range(t):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

dfs(1)
print(cnt)
