# https://www.acmicpc.net/problem/9017 : 크로스 컨트리 (python3)
# 2023-09-23
from sys import stdin
from collections import deque

input = stdin.readline

n = int(input())

for i in range(n):
    t = int(input())
    tt = list(map(int, input().split()))
    team = list(set(tt))
    team.sort()

    # 이중 배열을 만들어서 0,1,2,3로 배열을 생성
    
    for i in range(n):
        if tt in 
