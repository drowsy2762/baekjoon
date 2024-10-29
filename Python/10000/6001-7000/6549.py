# https://www.acmicpc.net/problem/6549 : 히스토그램에서 가장 큰 직사각형 (python3)
from sys import stdin

input = stdin.readline

while True:
    n = list(map(int, input().split()))
    arr = [0] * len(n) * 4
    if n[0] == 0:
        break
    max_extent = 0
    for i in len(n) - 2:
        h = 0


# 구간합을 구해야할때 = 보다 낮아졌을떄
# 그러면 좌 한번 우 한번 두번구해야함
