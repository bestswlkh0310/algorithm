while True:
    a, b = map(int, input().split())

    if a + b == 0: exit(0)

    a = max(1, a)

    arr = [1, 1]
    l = min(a, len(arr))

    while arr[-1] <= b:
        fivo = arr[-1] + arr[-2]
        arr.append(fivo)
        if arr[-1] < a:
            l = len(arr)
    
    print(len(arr) - l - 1)
    
    # 1 2 3 5 8 13 21 34 55 89