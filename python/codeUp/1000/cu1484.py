# 1484 달팽이 배열 채우기 4-1
n, m = map(int, input().split())
d = 0
arr = [[-1] * m for i in range(n)]
xPos = 0; yPos = 0
s = 1
arr[yPos][xPos] = s
c = 1
s += c
while s != n * m + 1:
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
        arr[dy][dx] = s
        s += c
    else:
        d += 1
        if d == 4: d = 0

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
    
    