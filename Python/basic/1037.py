n = int(input())
a = list(map(int,input().split()))
a.sort()
l = len(a)
print(a[0]*a[l-1])