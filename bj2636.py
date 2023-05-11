import collections
n, m = map(int, input().split())

arr = []
visit = [[False] * m for i in range(n)]
for i in range(n):
    arr.append(list(map(int, input().split())))
q = collections.deque()
q.append((0, 0, 0))

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

while q:
    (y, x, n1) = q.popleft()
    for i in dxy:
        xw = x + i[0]
        yw = y + i[1]
        if 0 <= yw < n and 0 <= xw < m:
            if arr[yw][xw] == 1 and not visit[y][x]:
                visit[yw][xw] = True
                q.append((yw, xw, n1 + 1))

            if arr[yw][xw] == 0:
                visit[yw][xw] = True
                q.append((yw, xw, n1))
for i in arr:
    for j in i:
        print("%2d" %j, end=" ")
    print()