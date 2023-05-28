a, b = map(int, input().split())
arr = []

for i in range(a):
    arr.append(list(input()))
v = 9999
def check(arr,  x1, y1):
    sum1 = 64
    sum2 = 64
    for i in range(8):
        for j in range(8):
            if i % 2 == 0:
                if (arr[i + y1][j + x1] == 'W') and ((i * 8 + j + 1) % 2 == 0): sum1 -= 1
                if (arr[i + y1][j + x1] == 'B') and ((i * 8 + j + 1) % 2 == 1): sum1 -= 1
                if ((arr[i + y1][j + x1] == 'W') and ((i * 8 + j + 1) % 2 == 1)): sum2 -= 1
                if ((arr[i + y1][j + x1] == 'B') and ((i * 8 + j + 1) % 2 == 0)): sum2 -= 1
            else:
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 1: sum1 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 0: sum1 -= 1
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 0: sum2 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 1: sum2 -= 1
    return min(sum1, sum2)

for i in range(a - 7):
    for j in range(b - 7):
        v = min(check(arr, j, i), v)
print(v)