while True:
    try:
        n = 3 ** int(input())

        arr = [True for _ in range(n)]

        def A(s, e):
            if s == e:
                return

            for j in range(s + (e - s) // 3, e - (e - s) // 3 - 1):
                arr[j] = False
            A(s, s + (e - s) // 3)
            A(e - (e - s) // 3, e)

        A(1, n)

        for i in arr:
            print(end=f"{'-' if i else ' '}")
        print()
    except:
        break