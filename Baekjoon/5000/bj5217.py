for i in range(int(input())):
    n = int(input())
    arr = []
    print("Pairs for %d:" %n, end=" ")
    for i in range(1, n):
        if n - i < i:
            break
        if i != (n - i):
            arr.append((i, n - i))
    for (idx, j) in enumerate(arr):
        if idx < len(arr) - 1:
            print(j[0], j[1], end=", ")
        else:
            print(j[0], j[1], end="")
    print()