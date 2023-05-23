# 가운데를 말해요 : https://www.acmicpc.net/problem/1655 (python3)

# 순서대로 들어오는 수들을 배열에 등록하고 그 배열에 중간값을 추출
# input -> sort -> print(middle num) -> repeat
# 0 0 1 1 2 2 3 3 4 4

import sys
import heapq

n = int(sys.stdin.readline())
max_heap = []
min_heap = []

for _ in range(n):
    num = int(sys.stdin.readline())
    if len(max_heap) == len(min_heap):
        heapq.heappush(max_heap, (-num, num))
    else:
        heapq.heappush(min_heap, (num, num))

    if min_heap and max_heap[0][1] > min_heap[0][1]:
        max_value = heapq.heappop(max_heap)[1]
        min_value = heapq.heappop(min_heap)[1]
        heapq.heappush(max_heap, (-min_value, min_value))
        heapq.heappush(min_heap, (max_value, max_value))

    print(max_heap[0][1])
