# https://www.acmicpc.net/problem/20006 : 랭킹전 대기열 (python3)
# 2023-11-07
from sys import stdin

input = stdin.readline

p, m = map(int, input().split())
player = []
for _ in range(p):
    l, n = input().split()
    player.append((l, n))

player.sort(key=lambda x: x[1])
i, cycle = 0, 0
end = 0
if m > p:
    print("Waiting!")
while i < p:
    if i % m == 0 and p % m != 0 and end == 0 and (p - (m * cycle)) < m:
        print("Waiting!")
        end += 1
    if i % m == 0 and p >= m and (p - (m * cycle)) > m:
        print("Started!")
        cycle += 1
    print(player[i][0], player[i][1])
    i += 1
