for i in range(int(input())):
    s1 = 0
    s2 = 0
    for j in range(int(input())):
        a, b = map(float, input().split())
        s1 += a * b
        s2 += a
    print("%d %.1f" %(s2, s1 / s2))