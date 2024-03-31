# https://www.acmicpc.net/problem/2293 : 동전 1 (python3)
# 2024-03-31
from sys import stdin

input = stdin.readline


def dp(coins, k):
    dp = [0 for _ in range(k + 1)]
    dp[0] = 1
    for coin in coins:
        for i in range(coin, k + 1):
            dp[i] += dp[i - coin]
    print(dp[k])


def solution():
    n, k = map(int, input().split())
    coins = []
    for _ in range(n):
        coins.append(int(input()))
    dp(coins, k)


solution()
