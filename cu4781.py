import collections
w, h = map(int, input().split())
arr = []
q = collections.deque()
for i in range(h):
    arr.append(list(map(int, input().split())))
t = True
for i in range(h):
    for j in range(w):
        if arr[i][j] == 0:
            t = False
        if arr[i][j] == 1:
            q.append((i, j, 1))
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
while q:
    (y, x, n) = q.popleft()
    for k in dxy:
        x1 = x + k[0]
        y1 = y + k[1]
        if 0 <= x1 < w and 0 <= y1 < h and arr[y1][x1] == 0:
            arr[y1][x1] = n
            q.append((y1, x1, n + 1))
s = False
mx = 0
for i in arr:
    if 0 in i:
        s = True
    mx = max(mx, max(i))
if s:
    print("-1")
elif t:
    print("0")
else:
    print(mx)