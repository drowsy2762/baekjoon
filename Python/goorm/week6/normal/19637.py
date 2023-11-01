# https://www.acmicpc.net/problem/19637 : IF문 좀 대신 써줘
# 2023-11-02
from sys import stdin

input = stdin.readline

title = []
cp = []
# 10000 under WEAK, 100000 under NORMAL
# 1000000 under STRONG
n, m = map(int, input().split())
for i in range(n):
    title.append(input().split())
    title[i][1] = int(title[i][1])
for i in range(m):
    cp.append(int(input()))
