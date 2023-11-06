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
    if day == 0:
        return start
    else:
        return day


T = int(input())
for _ in range(T):
    N = int(input())
    days = list(map(int, input().split()))
    sequence, cnt = 0, 0
    start, money = 0, 0

    while sequence != N - 1:
        stock = []
        rtmp = sequence
        sequence = getMax(sequence, N)
        if rtmp == sequence:
            sequence += 1
            start += 1
            continue
        # print(start, sequence, "t")
        if start + 1 == sequence:
            stock.append(days[start])
        else:
            for i in range(start, sequence):
                stock.append(days[i])
        start = sequence
        # print(days[sequence], stock)
        for i in range(len(stock)):
            money += days[sequence] - stock[i]
        stock = 0
    print(money)
