import collections

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
w, h = map(int, input().split())
arr = []
for i in range(h):
    arr.append(list(input().split()))

cnt = 0
for i in range(h):
    for j in range(w):
        if arr[i][j] == 'L':
            q = collections.deque()
            q.append((i, j))
            cnt += 1
            while q:
                (y, x) = q.popleft()
                for k in dxy:
                    x1 = x + k[0]
                    y1 = y + k[1]
                    if 0 <= x1 < w and 0 <= y1 < h and arr[y1][x1] == 'L':
                        q.append((y1, x1))
                        arr[y1][x1] = '.'
print(cnt)