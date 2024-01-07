for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    arr = []
    s1 = 0
    s2 = 0
    s3 = 0
    for _ in range(int(input())):
        cx, cy, r = map(int, input().split())
        d1 = ((x1 - cx) ** 2 + (y1 - cy) ** 2) ** 0.5
        d2 = ((x2 - cx) ** 2 + (y2 - cy) ** 2) ** 0.5
        # print('d1, d2', d1, d2)
        if d1 < r and d2 < r:
            pass
        elif d1 < r:
            s1 += 1
        elif d2 < r:
            s2 += 1

    print(s1 + s2 - s3)
