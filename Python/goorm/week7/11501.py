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


T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    sequence, j = 0, 0
    start, money, jusik = 0, 0, 0
    while sequence != N - 1:
        rtmp = sequence
        sequence = getMax(sequence, N)
        if rtmp == sequence:
            sequence += 1
            continue
        for i in range(start, sequence):
            jusik += days[i]
            j += 1
        start = sequence
        print(sequence, days[sequence], jusik, start, j)
        money += abs((days[sequence] - jusik)) * j
        jusik, j = 0, 0
    print(money, "t")
