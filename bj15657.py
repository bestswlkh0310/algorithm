a, b = map(int, input().split())
arr = sorted(list(map(int, input().split())))


def A(ar, n):
    if n != b:
        mx = max(ar)
    else:
        mx = 1
    if n == 0:
        for i in ar:
            print(i, end=" ")
        print()
        return
    for idx in range(a):
        newArr = ar[:]
        if arr[idx] >= mx:
            newArr.append(arr[idx])
            A(newArr, n - 1)

A([], b)