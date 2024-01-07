from collections import deque
I=lambda: [*map(int,input().split())]
h, w = I()
a=[I()for _ in range(h)]
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

t = True
s = None

for i in range(h):
    for j in range(w):
        if a[i][j] == 2:
            t = False
            s = (i, j, 3)
            break
    if not t:break

q = deque([s])

while q:
    (y, x, c) = q.popleft()
    for (dy, dx) in dxy:
        y1 = y + dy
        x1 = x + dx
        if 0 <= x1 < w and 0 <= y1 < h and a[y1][x1] == 1:
            a[y1][x1] = c
            q.append((y1, x1, c + 1))

for i in a:
    for j in i:
        if j == 0:
            print(end='0 ')
        else:
            print(end=f'{j - 2} ')
    print()