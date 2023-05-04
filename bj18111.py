import sys

y, x, b = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(y)]
minTime = sys.maxsize
h = 0
for i in range(257):
    time = 0
    m = 0
    n = 0
    for y1 in range(y):
        for x1 in range(x):
            if arr[y1][x1] > i:
                m += arr[y1][x1] - i
            else:
                n += i - arr[y1][x1]
    inventory = m + b - n
    if inventory >= 0 and 0 <= m * 2 + n <= minTime:
        minTime = m * 2 + n
        h = i
print(minTime, h)
