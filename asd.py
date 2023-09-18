n, t, c, p = map(int, input().split())
result = 0
arr = [0] * c
for i in range(n):
    for j in range(c):
        if arr[j] == t:
            arr[j] = 0
            result += p
        arr[j] += 1
print(result)
