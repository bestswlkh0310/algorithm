import collections
n, m, k = map(int, input().split())
arr = [[False] * (m) for i in range(n)]
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            arr[y][x] = True

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
cntArr = []
result = 0
for i in range(n):
    for j in range(m):
        if not arr[i][j]:
            arr[i][j] = True
            q = collections.deque()
            q.append((i, j))
            cnt = 1
            result += 1
            while q:
                (y, x) = q.popleft()
                for k in dxy:
                    dy = y + k[0]
                    dx = x + k[1]
                    if 0 <= dy < n and 0 <= dx < m and not arr[dy][dx]:
                        cnt += 1
                        arr[dy][dx] = True
                        q.append((dy, dx))
            cntArr.append(cnt)
print(result)

for i in sorted(cntArr):
    print(i, end=" ")