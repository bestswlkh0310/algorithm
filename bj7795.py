for _ in range(int(input())):
    n, m = map(int, input().split())
    aLst = list(map(int, input().split()))
    bLst = list(map(int, input().split()))

    cnt = 0
    for i in aLst:
        for j in bLst:
            if i > j:
                cnt += 1

    print(cnt)