import sys
import collections

m, n, h = map(int, sys.stdin.readline().split())
arr = []
q = collections.deque()
isZero = False
for i in range(h):
    s = []
    for j in range(n):
        lst = list(map(int, sys.stdin.readline().split()))
        for k in range(m):
            if lst[k] == 0:
                isZero = True
            if lst[k] == 1:
                q.append([i, j, k, 1])
        s.append(lst)
    arr.append(s)
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

w = True
mx = 0

while q:
    xyz = q.popleft()
    z = xyz[0]
    y = xyz[1]
    x = xyz[2]
    g = xyz[3]
    for i in range(6):
        z1 = z + dz[i]
        y1 = y + dy[i]
        x1 = x + dx[i]
        if 0 <= x1 < m and 0 <= y1 < n and 0 <= z1 < h and not arr[z1][y1][x1]:
            arr[z1][y1][x1] = g
            if arr[z1][y1][x1] > mx: mx = arr[z1][y1][x1]
            q.append([z1, y1, x1, g + 1])

for i in arr:
    for j in i:
        for k in j:
            if not k:
                w = False

if not isZero:
    print(0)
elif w:
    print(mx)
else:
    print(-1)
