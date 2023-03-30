n = int(input())
for _ in range(n) :
    C = 0
    G = 0.0
    t = int(input())
    for _ in range(t) :
        a, b = input().split()
        C += int(a)
        G += float(b)
    print(C,end=" ")
    if (G / float(t)) < 0.7 :
        print("0.0")
    elif (G / float(t)) < 1 :
        print("0.7")
    elif (G / float(t)) < 1.3 :
        print("1.0")
    elif (G / float(t)) < 1.7 :
        print("1.3")
    elif (G / float(t)) < 2 :
        print("1.7")
    elif (G / float(t)) < 2.3 :
        print("2.0")
    elif (G / float(t)) < 2.7 :
        print("2.3")
    elif (G / float(t)) < 3 :
        print("2.7")
    elif (G / float(t)) < 3.3 :
        print("3.0")
    elif (G / float(t)) < 3.7 :
        print("3.3")
    elif (G / float(t)) < 4 :
        print("3.7")
    elif (G / float(t)) < 4.3 :
        print("4.0")
    else :
        print("4.3")
    