n = int(input())

arr = [0] * 50
arr[1] = 1
arr[2] = 1
i = 2
cnt = 0
while i < n:
    arr[i] = arr[i - 1] + arr[i - 2] + 1
    i += 1
    cnt += 1

print(arr[n - 2] + 1, cnt)