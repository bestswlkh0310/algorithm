n = int(input())
if n == 1: 
    print(1)
    exit(0)

arr = [0 for _ in range(n)]
arr[0] = 1
arr[1] = 1
for i in range(2, n):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[-1])