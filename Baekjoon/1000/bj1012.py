import collections
for a in range(int(input())):
    w, h, k = map(int, input().split())
    arr = [[False] * w for i in range(h)]

    for i in range(k):
        x, y = map(int, input().split())
        arr[y][x] = True

    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j]:
                arr[i][j] = False
                q = collections.deque()
                q.append((i, j))
                cnt += 1
                while q:
                    (y1, x1) = q.popleft()
                    for k in dxy:
                        mx = x1 + k[0]
                        my = y1 + k[1]
                        if 0 <= mx < w and 0 <= my < h and arr[my][mx]:
                            arr[my][mx] = False
                            q.append((my, mx))
    print(cnt)