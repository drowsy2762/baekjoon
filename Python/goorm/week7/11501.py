# https://www.acmicpc.net/problem/11501 : 주식 (python3)
# 2023-11-08
from sys import stdin

input = stdin.readline


def getMax(start, end):
    max = 0
    day = 0
    for i in range(start, end):
        if days[i] > max:
            max = days[i]
            day = i
    return day


def buy():
    return


T = int(input())

for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    tmp, j = 0, 0
    start, money, jusik = 0, 0, 0
    while tmp != N - 1:
        rtmp = tmp
        tmp = getMax(tmp, N)
        if rtmp == tmp:
            tmp += 1
            continue
        for i in range(start, tmp - 1):
            jusik += days[i]
            j += 1
        money += jusik * days[tmp] - jusik
        jusik = 0
    print(money, "t")
