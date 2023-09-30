# https://www.acmicpc.net/problem/1157 : 단어 공부 (python3)
# 2023-09-14
# input 최적화 작업
from sys import stdin

input = stdin.readline

s = input().lower()
s_l = list(set(s))
cnt = []

for i in s_l:
    cnt.append(s.count(i))

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(s_l[cnt.index(max(cnt))].upper())

# 딱히 주석이 필요없는 문제
