n = int(input())

arr = [[1 if i == j or i == 0 else 0 for i in range(n)] for j in range(n)]


for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i - 1][j - 1] + arr[i - 1][j]

for i in range(n):
    for j in range(i + 1):
        print(end=f"{arr[i][j]} ")
    print()