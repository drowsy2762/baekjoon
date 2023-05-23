# 가운데를 말해요 : https://www.acmicpc.net/problem/1655 (python3)

# 순서대로 들어오는 수들을 배열에 등록하고 그 배열에 중간값을 추출
# input -> sort -> print(middle num) -> repeat
# 0 0 1 1 2 2 3 3 4 4

import sys


def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)


n = int(input())
k = []
for i in range(n):
    k.append(int(input()))
    k.sort()
    print(k[int(i / 2)])
