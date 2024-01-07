# 1477 빗금 채우기 3-2
n, m = map(int, input().split())
xPos = 0
yPos = 0
arr = [[0 for i in range(m)] for i in range(n)]
s = 1
arr[yPos][xPos] = s
xS = 0

#
# def show():
#     print(yPos, xS)
#     for i in arr:
#         for j in i:
#             print(j, end=' ')
#         print()
#     print("---------------")

for i in range(n + m):
    xPos = i
    if xPos >= m:
        xPos = m - 1
        xS += 1
    for j in range(n + m):
        yPos = j + xS
        if 0 <= yPos < n and 0 <= xPos < m:
            # show()
            arr[yPos][xPos] = s
            s += 1
            xPos -= 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()