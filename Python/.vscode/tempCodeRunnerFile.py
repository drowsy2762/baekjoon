a = []
for i in range(8):
    n = int(input())
    a.append(n)
b = a
a.sort()
sum = 0
for i in range(5):
    sum += a[7-i]
print(sum)
for i in range(8):
    if(b[i]>=a[3]):
        print(i,end=' ')