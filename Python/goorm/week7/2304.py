# https://www.acmicpc.net/problem/2304 : 창고 다각형(python3)
# 2023-11-10
from sys import stdin

input = stdin.readline

n = int(input())

storage = list()
area = 0
l, m = map(int, input().split())
x = l
ymax = m
for _ in range(n - 1):
    l, m = map(int, input().split())
    storage.append((l, m))
storage.sort()
for i, k in storage:
    print((i - x) * ymax, "t")
    area += (i - x) * ymax
    if ymax < k:
        ymax = k
    x = i
area += ymax
storage.reverse()
smax = k
x += 1
for i, k in storage:
    area -= (x - i) * (ymax - smax)
    print((x - i) * (ymax - smax))
    x = i
    if k > smax:
        smax = k
    if smax == ymax:
        break
print(area)
# print(storage)
