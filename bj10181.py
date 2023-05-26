while True:
    n = int(input())
    if n == -1:
        break
    arr = []
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    s = sum(arr)
    if n == s:
        print(f"{n} = 1", end="")
        del arr[0]
        for i in arr:
            print(f" + {i}", end="")
    else:
        print(f"{n} is NOT perfect.", end="")
    print()