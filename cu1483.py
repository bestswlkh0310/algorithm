# 1483 빗금 채우기 3-8
n, m = map(int, input().split())
xPos = 0
yPos = 0
arr = [[0 for i in range(m)] for i in range(n)]
s = 1
arr[yPos][xPos] = s
yS = 1

for i in range(n + m):
    yPos = i
    if yPos >= n:
        yPos = n - 1
        yS += 1
    for j in range(n + m):
        xPos = j
        if 0 <= yPos < n and 0 <= xPos + yS - 1 < m:
            arr[n - yPos - 1][xPos + yS - 1] = s
            s += 1
            yPos -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()