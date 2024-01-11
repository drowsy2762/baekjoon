# https://www.acmicpc.net/problem/2138 : 전구와 스위치 (python3)
# 2024-01-12
from sys import stdin

input = stdin.readline


n = int(input())
bulb = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))


def change(A, B):
    A_copy = A[:]
    press = 0
    for i in range(1, n):
        if A_copy[i - 1] == B[i - 1]:
            continue

        press += 1
        for j in range(i - 1, i + 2):
            if j < n:
                A_copy[j] = 1 - A_copy[j]
    if A_copy == B:
        return press
    else:
        return 1e9


res = change(bulb, target)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
if res != 1e9:
    print(res)
else:
    print(-1)
