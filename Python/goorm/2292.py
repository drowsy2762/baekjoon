# https://www.acmicpc.net/problem/2292 : 벌집 (python3)
# 2023-09-13
# input 최적화 작업
from sys import stdin

input = stdin.readline

n = int(input())

# 1번 방부터 시작
room = 1
# 1번 방은 1개
cnt = 1
# 방이 6의 배수로 늘어남
# 1번 방을 제외한 6의 배수마다 방이 늘어남
while n > room:
    room += 6 * cnt
    cnt += 1

print(cnt)
