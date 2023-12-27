for i in range(int(input())):
    arr = []
    ss = 0
    for j in range(int(input())):
        arr.append(int(input()))
    l = len(arr)
    t = False
    for j in range(1, max(arr) + 1):
        ar = []
        if t: break
        for k in arr:
            ar.append(k % j)
        if len(set(ar)) == l:
            ss = j
            t = True
            break
    print(ss)