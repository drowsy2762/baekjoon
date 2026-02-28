# https://www.acmicpc.net/problem/15591
# 2026-02-28
import sys
from collections import deque
input = sys.stdin.readline

n, Q = map(int, input().split())
relationships = [[] for _ in range(n+1)]

for _ in range(n - 1):
    u, v, r = map(int, input().split())
    relationships[u].append((v, r))
    relationships[v].append((u, r))

for _ in range(Q):
    k, start_v = map(int, input().split())
    visited = [False] * (n + 1)
    visited[start_v] = True
    result = 0
    
    dq = deque([start_v])

    while dq:
        curr_v = dq.pop()
        for next_v, next_usado in relationships[curr_v]:
            if next_usado >= k and not visited[next_v]:
                result += 1
                dq.append(next_v)
                visited[next_v] = True
                
    print(result)