import collections
import sys
h, w = map(int, sys.stdin.readline().split())
arr = []

for i in range(h):
    arr.append(list(map(int, sys.stdin.readline().split())))
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
s = 0
day = -1
e = False
while True:
    day += 1
    s = 0
    t = True
    chkArr = [i[:] for i in arr]
    wArr = [[0] * w for i in range(h)]
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 0: continue
            for k in dxy:
                x1 = j + k[0]
                y1 = i + k[1]
                if 0 <= x1 < w and 0 <= y1 < h and arr[y1][x1] == 0:
                    t = False
                    wArr[i][j] += 1
    for i in range(h):
        for j in range(w):
            if arr[i][j] < wArr[i][j]:
                arr[i][j] = 0
            else:
                arr[i][j] -= wArr[i][j]
    for i in range(h):
        for j in range(w):
            if chkArr[i][j] != 0:
                s += 1
                chkArr[i][j] = 0
                q = collections.deque()
                q.append((i, j))
                while q:
                    (y, x) = q.popleft()
                    for k in dxy:
                        x1 = x + k[0]
                        y1 = y + k[1]
                        if 0 <= x1 < w and 0 <= y1 < h and chkArr[y1][x1] != 0:
                            chkArr[y1][x1] = 0
                            q.append((y1, x1))
    if s >= 2:
        e = True
        break
    if s == 0 or (s != 0 and t):
        break
if e:
    if day == 0:
        print(1)
    else:
        print(day)
else:
    print(0)