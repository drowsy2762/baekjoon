# https://www.acmicpc.net/problem/2164 : 카드2(python3)
# 2023-10-04

from sys import stdin
from collections import deque

n = int(input())

card = deque()
for i in range(n):
    card.append(i)

while len(card) != 1:
    card.popleft()
    t = card.popleft()
    card.append(t)

print(card[0] + 1)
