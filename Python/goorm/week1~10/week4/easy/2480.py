# https://www.acmicpc.net/problem/2480 : 주사위 세개 (python3)
# 2021-10-03

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b:
    print(1000 + a * 100)
elif a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)
