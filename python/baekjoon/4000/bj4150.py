n = int(input())

arr = [0 for _ in range(max(2, n))]

arr[0] = 1
arr[1] = 1

for i in range(2, n):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[-1])