# https://www.acmicpc.net/problem/2525 : 오븐 시계 (python3)
# 2021-10-02

hour, minute = map(int, input().split())
cooking_time = int(input())

hour += cooking_time // 60
minute += cooking_time % 60

if minute >= 60:
    hour += 1
    minute -= 60

if hour >= 24:
    hour -= 24

print(hour, minute)
