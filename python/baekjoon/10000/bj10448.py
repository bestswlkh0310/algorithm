for q in range(int(input())):
    n = int(input())
    t = False
    for i in range(1, n + 1):
        if i * (i + 1) / 2 > n: break
        if t: break
        for j in range(1, n + 1):
            if j * (j + 1) / 2 > n: break
            if t: break
            for k in range(1, n + 1):
                if k * (k + 1) / 2 > n: break
                if i * (i + 1) / 2 + j * (j + 1) / 2 + k * (k + 1) / 2 == n:
                    t = True
                    break
    if t: print(1)
    else: print(0)