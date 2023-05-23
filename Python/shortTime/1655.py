# 가운데를 말해요 : https://www.acmicpc.net/problem/1655 (python3)

# 순서대로 들어오는 수들을 배열에 등록하고 그 배열에 중간값을 추출
# input -> sort -> print(middle num) -> repeat
# 0 0 1 1 2 2 3 3 4 4

import sys
import heapq


def heapqsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result


n = int(sys.stdin.readline().rstrip())
k = []
cnt = 0
for i in range(n):
    k.append(int(sys.stdin.readline().rstrip()))
    k = heapqsort(k)
    if i % 2 == 0:
        cnt += 1
    print(k[cnt - 1])
