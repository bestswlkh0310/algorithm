for q in range(int(input())):
    a = []
    n = int(input())
    mx = -1
    mxIdx = 0

    for i in range(n):
        k, s = input().split()
        a.append(s)
        if mx < int(k):
            mx = int(k)
            mxIdx = i
    print(a[mxIdx])