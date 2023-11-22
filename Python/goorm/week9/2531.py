# https://www.acmicpc.net/problem/2531 : 회전 초밥 (python3)
# 2023-11-23
from sys import stdin

input = stdin.readline

N, d, k, c = map(int, input().split())
belts = []
cases = []
M = 0

# 회전 벨트에 올라와있는 초밥번호를 받음
for _ in range(N):
    belts.append(int(input()))

# 슬라이스를 연장
for i in range(k):
    belts.append(belts[i])

# 중복값을 걸러냄
for i in range(N):
    tmp = belts[i : i + k]
    list1 = list(dict.fromkeys(tmp))
    if len(list1) == k:
        cases.append(belts[i : i + k])

print(cases)
# print(cases)

# cnt = 0
# for i in cases:
#     cnt = 0
#     for j in i:
#         if j == c:
#             cnt = 1
#             break
#     if cnt == 0:
#         cnt = 1
#     else:
#         cnt = 0
#     M = max(M, k + cnt)


print(M)
