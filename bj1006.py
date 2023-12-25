for _ in range(int(input())):
    n, w = map(int, input().split())
    arr = []
    arr.extend(list(map(int, input().split())))
    arr.extend(list(map(int, input().split())))

    cnt1 = 0

    print(arr)

    for (idx, i) in enumerate(arr):
        def insert(idx1):
            global cnt1
            cnt1 += 1
            arr[idx1] = None
            arr[idx] = None

        if arr[idx] == None:
            continue
        if idx < n:
            if arr[(idx + 1) % n] != None and i + arr[(idx + 1) % n] <= w:
                insert((idx + 1) % n)
            elif arr[(idx - 1) % n] != None and i + arr[(idx - 1) % n] <= w:
                insert((idx - 1) % n)
        elif idx >= n:
            if arr[(idx + 1 - n) % n + n] != None and i + arr[(idx + 1 - n) % n + n] <= w:
                insert((idx + 1 - n) % n + n)
            elif arr[(idx - 1 - n) % n + n] != None and i + arr[(idx - 1 - n) % n + n] <= w:
                insert((idx - 1 - n) % n + n)
        if arr[idx] == None:
            continue
        if arr[(idx + n) % (n * 2)] != None and arr[(idx + n) % (n * 2)] + i <= w:
            insert((idx + n) % (n * 2))
    print(arr)
    print(cnt1 + len([i for i in arr if i != None]))
    