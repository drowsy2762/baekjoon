# https://www.acmicpc.net/problem/10830 : 행렬제곱 (python3)
import sys
import copy

input = sys.stdin.readline


def matmul(a, b, m, t):
    sum = 0
    for i in range(len(m)):
        sum += t[a][i] * m[i][b]
    return sum


n, b = map(int, input().split())
m = []
for i in range(n):
    m.append(list(map(int, input().split())))
r = copy.deepcopy(m)
for _ in range(b - 1):
    t = copy.deepcopy(r)
    for i in range(n):
        for j in range(n):
            r[i][j] = matmul(i, j, m, t)
for i in range(n):
    for j in range(n):
        while r[i][j] > 1000:
            r[i][j] %= 1000
        print(r[i][j], end=" ")
    print()
