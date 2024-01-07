while True:
    try:
        n = int(input())
        k = 1
        while True:
            s = int("1" * k)
            if s % n == 0:
                x = list(map(int, (list(str(s)))))
                print(len(x) - x.index(min(x)))
                break
            k += 1
    except:
        break