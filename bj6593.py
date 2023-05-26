import collections
while True:
    h, w, s = map(int, input().split())
    if h == 0 and w == 0 and s == 0:
        break
    arr = [[] for i in range(h)]
    for i in range(h):
        for j in range(w):
            arr[i].append(list(input()))
        input()
    dxyz = ((0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0))
    ep = None
    q = collections.deque()
    for i in range(h):
        for j in range(w):
            for k in range(s):
                if arr[i][j][k] == 'S':
                    q.append((i, j, k, 1))
                    arr[i][j][k] = 1
    r = -1
    while q:
        (y, x, z, n) = q.popleft()
        for k in dxyz:
            y1 = y + k[0]
            x1 = x + k[1]
            z1 = z + k[2]
            # print(y1, x1, z1)
            if 0 <= y1 < h and 0 <= x1 < w and 0 <= z1 < s:
                if arr[y1][x1][z1] == '.':
                    arr[y1][x1][z1] = n
                    q.append((y1, x1, z1, n + 1))
                if arr[y1][x1][z1] == 'E':
                    r = n
                    break
    if r == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {r} minute(s).")