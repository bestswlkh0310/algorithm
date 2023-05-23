import collections
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1))
while True:
    cnt = 0
    w, h = map(int, input().split())
    if h == 0 and w == 0:
        break
    arr = []
    for i in range(h):
        arr.append(list(map(int, input().split())))
    q = collections.deque()
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = 0
                q.append((i, j))
                while q:
                    (y, x) = q.popleft()
                    for k in dxy:
                        mx = x + k[0]
                        my = y + k[1]
                        if 0 <= mx < w and 0 <= my < h and arr[my][mx] == 1:
                            arr[my][mx] = 0
                            q.append((my, mx))
    print(cnt)
    # print(arr)