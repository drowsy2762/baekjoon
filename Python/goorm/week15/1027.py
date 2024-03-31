# https://www.acmicpc.net/problem/1027 : 고층 건물 (python3)
# 2024-02-21
from sys import stdin

input = stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
answer = [0] * n
