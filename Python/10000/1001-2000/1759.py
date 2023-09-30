# https://www.acmicpc.net/problem/1759 : 암호 만들기 (python3)
from sys import stdin

input = stdin.readline

l, c = map(int, input().split())
alphabet = list(input().split())

alphabet.sort()

print(alphabet)
