# https://www.acmicpc.net/problem/2531 : 회전 초밥 (python3)
# 2023-11-23
from sys import stdin

input = stdin.readline

N, d, k, c = map(int, input().rsplit())
belts = [int(input().rstrip()) for _ in range(N)]
belts.extend(belts)
left, right = 0, 0

answer = 0

while left != N:
    right = left + k
