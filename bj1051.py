h, w = map(int, input().split())

arr = [list(map(int, list(input()))) for _ in range(h)]

# print(arr)
mn = min(h, w)

result = 0

for i in range(mn):
    for k in range(w - i):
        for j in range(h - i):
            # print(i, j, k)
            if arr[j + i][k + i] == arr[j][k] and arr[j][k] == arr[j + i][k] and arr[j][k] == arr[j][k + i]:
                v = (i + 1) ** 2
                if result < v:
                    result = v

print(result)