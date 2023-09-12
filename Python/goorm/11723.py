# https://www.acmicpc.net/problem/11723 : 집합 (python3)
# 2023-09-15
# input 최적화 작업

from sys import stdin

input = stdin.readline

m = int(input())
s = set()

for _ in range(m):
    cmd = input().split()
    # add 처리
    if cmd[0] == "add":
        s.add(int(cmd[1]))
    # remove 처리
    elif cmd[0] == "remove":
        s.discard(int(cmd[1]))
    # check 처리
    elif cmd[0] == "check":
        if int(cmd[1]) in s:
            print(1)
        else:
            print(0)
    # toggle 처리
    elif cmd[0] == "toggle":
        if int(cmd[1]) in s:
            s.discard(int(cmd[1]))
        else:
            s.add(int(cmd[1]))
    # all 처리
    elif cmd[0] == "all":
        s = set(range(1, 21))
    # empty 처리
    elif cmd[0] == "empty":
        s = set()
