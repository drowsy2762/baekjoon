# 2026-09-10
from collections import deque


def solution(priorities, location):
    queue = deque([(priority, idx) for idx, priority in enumerate(priorities)])
    execution_order = 0
    while queue:
        cur_priority, cur_idx = queue.popleft()
        if any(other_priority > cur_priority for other_priority, _ in queue):
            queue.append((cur_priority, cur_idx))
        else:
            execution_order += 1
            if cur_idx == location:
                return execution_order
