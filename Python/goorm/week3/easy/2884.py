# https://www.acmicpc.net/problem/2884 : 알람 시계 (python3)
# 2021-09-29

h, m = map(int, input().split())

if m >= 45:
    print(h, m - 45)
elif m < 45 and h > 0:
    print(h - 1, m + 15)
else:
    print(23, m + 15)
