# https://www.acmicpc.net/problem/11501 : 주식 (python3)
# 2023-11-08
from sys import stdin

input = stdin.readline


def getMax(start, end):
    max, day = 0, 0
    for i in range(start, end):
        if days[i] > max:
            max = days[i]
            day = i
    if day == 0:
        return start
    else:
        return day


def sell(start, end):
    money = 0
    for i in range(start, end):
        money += days[end] - days[i]
    return money


T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    sequence = 0
    start, money = 0, 0

    while sequence != N - 1:
        rtmp = sequence
        sequence = getMax(sequence, N)
        if rtmp == sequence:
            sequence += 1
            start = sequence
            continue
        money += sell(start, sequence)
        start = sequence
    print(money)
