for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    x1 = 1
    y1 = 1
    cnt = 1
    while True:
        if x1 == x and y1 == y:
            break
        x1 += 1
        y1 += 1
        if x1 == m + 1: x1 = 1
        if y1 == n + 1: y1 = 1
        cnt += 1
        if cnt > m * n:
            cnt = -1
            break
    print(cnt)