# https://www.acmicpc.net/problem/2512 : 예산 (python3)
# 2023-10-09

from sys import stdin

input = stdin.readline

n = int(input())
request = list(map(int, input().split()))
budget = int(input())

Max, m = 0, 0
Sum = sum(request)

if budget >= Sum:
    for i in range(n):
        Max = max(request[i], Max)
    print(Max)
else:
    Average = int(Sum / n)
    for i in range(n):
        if request[i] < Average:
            budget -= request[i]
            m += 1
    print(int(budget / m))
