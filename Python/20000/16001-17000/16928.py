# https://www.acmicpc.net/problem/16928 : 뱀과 사다리 게임 (python3)
# 2024-03-28
from sys import stdin
from collections import deque


def bfs(ladder, snake):
    visited = [False for _ in range(101)]
    graph = [0 for _ in range(101)]
    q = deque([1])
    while q:
        t = q.popleft()

        if t == 100:
            print(graph[t])
            break
        for dice in range(1, 7):
            x = t + dice
            if x <= 100 and not visited[x]:
                if x in ladder.keys():
                    x = ladder[x]
                if x in snake.keys():
                    x = snake[x]
                if not visited[x]:
                    visited[x] = True
                    graph[x] = graph[t] + 1
                    q.append(x)


def solution():
    input = stdin.readline

    n, m = map(int, input().split())
    ladder = dict()
    snake = dict()
    for _ in range(n):
        i, j = map(int, (input().split()))
        ladder[i] = j
    for _ in range(m):
        i, j = map(int, (input().split()))
        snake[i] = j

    bfs(ladder, snake)


solution()
