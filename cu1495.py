# 1495 차이 배열 만들기
n, m, k = map(int, input().split())
arr = [[0] * (m + 1) for i in range(n + 1)]
for i in range(k):
    x1, y1, x2, y2, u = map(int, input().split())
    arr[x1][y1] += u
    arr[x2 + 1][y2 + 1] += u
    arr[x1][y2 + 1] -= u
    arr[x2 + 1][y1] -= u
for i in range(n):
    del arr[i][-1]
del arr[-1]
for i in arr:
    for j in i:
        print(j, end=" ")
    print()
print()
for i in range(n):
    for j in range(m):
        s = 0
        for k in range(i + 1):
            for l in range(j + 1):
                s += arr[k][l]
        print(s, end=" ")
    print()
