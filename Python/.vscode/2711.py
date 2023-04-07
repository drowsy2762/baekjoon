n = int(input())

for i in range(n):
    a = list(input().split())
    result = a[1][int(a[0]):int(a[0])]
    print(result)