a, b = map(int, input().split())
mx = max(a, b)
arr = [[1] * mx for i in range(mx)]

for i in range(2, mx):
    for j in range(1, i):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]
print(arr[mx - 1][min(a, b) - 1])