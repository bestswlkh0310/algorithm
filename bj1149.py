n = int(input())

arr = []

for i in range(n):
    lst = list(map(int, input().split()))
    arr.append(lst)
    if i == 0:
        continue
    for j in range(3):
        mn = 99999
        for (idx, k) in enumerate(arr[-2]):
            if idx == j: continue
            if mn > k:
                mn = k
        # print(mn)
        arr[-1][j] += mn
    # print(arr)

print(min(arr[-1]))
