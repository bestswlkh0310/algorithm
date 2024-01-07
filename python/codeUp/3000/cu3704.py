n = int(input())

arr = [0 for _ in range(max(4, n))]
arr[0] = 1
arr[1] = 2
arr[2] = 4

for i in range(3, n):
    arr[i] = (arr[i - 1] + arr[i - 2] + arr[i - 3]) % 1000

print(arr[n - 1] % 1000)

# 1 1 1
# 1 2
# 2 1
# 3