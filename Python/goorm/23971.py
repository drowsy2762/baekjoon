# https://www.acmicpc.net/problem/23971 : ZOAC 4 (python3)
# input 최적화 작업
from sys import stdin

input = stdin.readline

# 1이 몇개들어가는지 세기
cnt = 0

h, w, n, m = map(int, input().split())

for i in range(0, h, n + 1):
    for j in range(0, w, m + 1):
        cnt += 1


print(cnt)
