a, b = map(int, input().split())
mx = max(a, b)
arr = [[1] * (mx + 1) for i in range(mx + 1)]

for i in range(1, mx + 1):
    for j in range(1, mx + 1):
        arr[i][j] = arr[i - 1][j] + arr[i][j - 1]
print(arr[a - 1][b - 1] % 100000000)