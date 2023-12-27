# 1481 빗금 채우기 3-6
n, m = map(int, input().split())
xPos = 0
yPos = 0
arr = [[0 for i in range(m)] for i in range(n)]
s = 1
arr[yPos][xPos] = s
xS = 0

for i in range(n + m):
    xPos = i
    if xPos >= m:
        xPos = m - 1
        xS += 1
    for j in range(n + m):
        yPos = j + xS
        if 0 <= yPos < n and 0 <= xPos < m:
            arr[n - yPos - 1][m - xPos - 1] = s
            s += 1
            xPos -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()