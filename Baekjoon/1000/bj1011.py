for _ in range(int(input())):
    s, e = map(int, input().split())

    v = e - s
    k = 0
    i = 1
    j = 1
    t = False

    while k < v:
        k += i
        if t:
            i += 1
            t = False
        else:
            t = True
        j += 1
    print(j - 1)