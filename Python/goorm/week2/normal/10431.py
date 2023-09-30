# https://www.acmicpc.net/problem/10431 : 주사위 세개 (python3)
# 2023-09-20
# input 최적화 작업
from sys import stdin

input = stdin.readline

p = int(input())


# 버블정렬
def b_sort(arr):
    cnt = 0
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                cnt += 1
    return cnt


for _ in range(p):
    arr = list(map(int, input().split()))
    # 배열을 분리
    count, people = arr[0], arr[1:]
    print(count, b_sort(people))
