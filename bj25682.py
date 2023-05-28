import sys
a, b, c = map(int, sys.stdin.readline().split())
arr = []

for i in range(a):
    arr.append(list(sys.stdin.readline()))
v = sys.maxsize
def check(arr,  x1, y1):
    sum1 = c ** 2
    sum2 = c ** 2
    for i in range(c):
        for j in range(c):
            if i % 2 == 0:
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 0: sum1 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 1: sum1 -= 1
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 1: sum2 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 0: sum2 -= 1
            else:
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 1: sum1 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 0: sum1 -= 1
                if arr[i + y1][j + x1] == 'W' and (i * 8 + j + 1) % 2 == 0: sum2 -= 1
                if arr[i + y1][j + x1] == 'B' and (i * 8 + j + 1) % 2 == 1: sum2 -= 1
    return min(sum1, sum2)

for i in range(a - c + 1):
    for j in range(b - c + 1):
        v = min(check(arr, j, i), v)
print(v)