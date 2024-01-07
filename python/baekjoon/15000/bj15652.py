# a b => a개 중 b개를 고르는 경우
a, b = map(int, input().split())
arr = [i for i in range(1, a + 1)]


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