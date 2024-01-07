n = int(input())
arr = [(0, '1') for _ in range(n + 1)]
for i in range(2, n + 1):
    arr[i] = (arr[i - 1][0] + 1, f'{i} ' + arr[i - 1][1])
    if i % 2 == 0:
        if arr[i//2][0] + 1 < arr[i][0]:
            arr[i] = (arr[i//2][0] + 1, f'{i} ' + arr[i//2][1])
    if i % 3 == 0:
        if arr[i//3][0] + 1 < arr[i][0]:
            arr[i] = (arr[i//3][0] + 1, f'{i} ' + arr[i//3][1])
print(arr[n][0])
print(arr[n][1])
