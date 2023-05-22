n = int(input())
arr = [[0] * (n + 1) for i in range(n)]

for i in range(n):
    lst = list(map(int, input().split()))
    for (idx, j) in enumerate(lst):
        arr[i][idx + 1] = j

for i in range(1, n):
    for j in range(i + 2):
        arr[i][j] += max(arr[i - 1][j], arr[i - 1][j - 1])
# for i in arr:
#     print(i)
print(max(arr[-1]))

# 3
# 1
# 2 3
# 1 5 2