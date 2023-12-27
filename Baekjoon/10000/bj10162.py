arr = [300, 60, 10]
result = [0, 0, 0]

n = int(input())
if n % 10 != 0: print(-1)
else:
    while n != 0:
        for i in range(3):
            if n - arr[i] >= 0:
                n -= arr[i]
                result[i] += 1
                break
    for i in range(3): print(result[i], end=" ")