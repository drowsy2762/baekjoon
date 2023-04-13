k = int(input())
data = []
for i in range(k):
    n = int(input())
    if(n != 0):
        data.append(n)
    else:
        data.pop()
print(sum(data))