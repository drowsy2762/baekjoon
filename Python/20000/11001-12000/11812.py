# https://www.acmicpc.net/problem/11812
# 2026-04-13
import sys

def solution():
    input = sys.stdin.readline

    def LCA(x, y):
        d = 0
        while x != y:
            if x > y:
                x = (x + k - 2) // k
            else:
                y = (y + k - 2) // k
            d += 1
        return d

    n, k, q = map(int, input().split())
    for _ in range(q):
        x, y = map(int, input().split())
        if k == 1:
            print(abs(x - y))
            continue
        print(LCA(x, y))
        
if __name__ == "__main__":
    solution()