a, b = map(int, input().split())
arr = sorted(list(map(int, input().split())))
visit = [False for i in range(1, a + 1)]


def A(ar, vi, n):
    if n == 0:
        for i in ar:
            print(i, end=" ")
        print()
        return
    for idx in range(a):
        if not vi[idx]:
            newArr = ar[:]
            newArr.append(arr[idx])

            newVi = vi[:]
            newVi[idx] = True
            A(newArr, newVi, n - 1)
            if idx < a - 1:
                vi[idx] = True

A([], visit, b)