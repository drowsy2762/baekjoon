# https://www.acmicpc.net/problem/17615 : 볼 모으기 (python3)
# 2023-11-22
from sys import stdin
from collections import deque

input = stdin.readline


def moving_R(s):
    # print(s, "R")
    cnt = 0
    while True:
        if s[0] != "R":
            s.append("B")
            s.popleft()
            # print(cnt, "t")
            cnt += 1
            # print(cnt, "t1")
        else:
            break
    i = 0
    status = 0
    lens = len(s)
    while True:
        if lens - 1 == i:
            break
        if s[i] != s[i + 1]:
            status += 1
        if status == 2:
            s.append(s[i])
            del s[i]
            cnt += 1
            status = 0
            i = 0
        i += 1
    # print(s)
    return cnt


def moving_B(s):
    cnt = 0
    while True:
        if s[0] != "B":
            s.append("R")
            s.popleft()
            # print(cnt, "t")
            cnt += 1
            # print(cnt, "t1")
        else:
            break
    i = 0
    status = 0
    lens = len(s)
    while True:
        if lens - 1 == i:
            break
        if s[i] != s[i + 1]:
            status += 1
        if status == 2:
            s.append(s[i])
            del s[i]
            cnt += 1
            status = 0
            i = 0
        i += 1
    # print(s)
    return cnt


n = int(input())
a = input().rstrip()
b = deque(a[:])
b.reverse()
a = deque(a)
# print(a, b)
print(min(moving_R(b), moving_B(a), moving_R(a), moving_B(b)))
