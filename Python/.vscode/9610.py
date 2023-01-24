n = int(input())
x = y = []
q1 = q2 = q3 = q4 = m = 0
for i in range(n) :
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)
    if(x[i] > 0 and y[i] > 0) :
        q1 += 1
    elif(x[i] > 0 and y[i] < 0) :
        q4 += 1
    elif(x[i] < 0 and y[i] > 0) :
        q2 += 1
    elif(x[i] < 0 and y[i] < 0) :
        q3 += 1
    else :
        m += 1

print("Q1: ",q1)
print("Q2: ",q2)
print("Q3: ",q3)
print("Q4: ",q4)
print("AXIS: ",m)