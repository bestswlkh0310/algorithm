# 1487 달팽이 배열 채우기 4-4
n, m = map(int, input().split())
d = 0
arr = [[-1] * m for i in range(n)]
xPos = m - 1
yPos = 0
s = m * n
arr[yPos][xPos] = s
c = -1
while s > 1:
    dx = xPos
    dy = yPos
    if d == 0:
        dx += 1
    elif d == 1:
        dy += 1
    elif d == 2:
        dx -= 1
    elif d == 3:
        dy -= 1
    if 0 <= dx < m and 0 <= dy < n and arr[dy][dx] == -1:
        xPos = dx
        yPos = dy
        s += c
        arr[dy][dx] = s
    else:
        d += 1
        if d == 4:
            d = 0

for i in arr:
    for j in i:
        print(j, end=" ")
    print()

