for i in range(int(input())):
    n, d = map(int, input().split())
    cnt = 0
    for j in range(n):
        v, f, c = map(int, input().split())
        if (f / c) * v >= d:
            cnt += 1
    print(cnt)