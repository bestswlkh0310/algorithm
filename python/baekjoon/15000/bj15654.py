n, k = map(int, input().split())
lst = sorted(map(int, input().split()))
visit = [False for i in range(1, n + 1)]
def A(ar, vi, n1):
    if n1 == 0:
        for d in ar:
            print(d, end=" ")
        print()

    for (idx, i) in enumerate(vi):
        if not i:
            newArr = ar[:]
            newArr.append(lst[idx])

            newVi = vi[:]
            newVi[idx] = True
            A(newArr, newVi, n1 - 1)

A([], visit, k)