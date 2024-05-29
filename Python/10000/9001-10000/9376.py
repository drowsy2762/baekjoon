# https://www.acmicpc.net/problem/9376 : 탈옥 (Python3)

from sys import stdin

input = stdin.readline


def jail_break():
    global jail
    h, w = map(int, input().split())
    jail = [list(input().rstrip()) for _ in range(h)]


def solution():
    n = int(input())
    for _ in range(n):
        jail_break()


solution()
