import collections
h, w = map(int, input().split())
arr = []
s = []
birus = collections.deque()

# def show(ls):
#     for i in ls:
#         for j in i:
#             print(j, end=" ")
#         print()

# 입력
for i in range(h):
    arr.append(list(map(int, input().split())))

# 방어벽 좌표 입력
for i in range(h):
    for j in range(w):
        if arr[i][j] != 0: continue
        for i1 in range(h):
            for j1 in range(w):
                if arr[i1][j1] != 0 or (i == i1 and j == j1): continue
                for i2 in range(h):
                    for j2 in range(w):
                        if arr[i2][j2] != 0 or (i == i2 and j == j2) or (i1 == i2 and j1 == j2): continue
                        s.append((i, j, i1, j1, i2, j2))
# 바이러스 찾기
for i in range(h):
    for j in range(w):
        if arr[i][j] == 2:
            birus.append([i, j])
d = ((0, 1), (0, -1), (1, 0), (-1, 0))
mx = 0
# 방어벽 설치 후 bfs
for i in s:
    (x1, y1, x2, y2, x3, y3) = i
    arr1 = [k[:] for k in arr]
    arr1[x1][y1] = 1
    arr1[x2][y2] = 1
    arr1[x3][y3] = 1
    q = birus.copy()
    # 탐색
    while q:
        (y, x) = q.popleft()
        for j in range(4):
            ym = y + d[j][0]
            xm = x + d[j][1]
            if 0 <= ym < h and 0 <= xm < w and not arr1[ym][xm]:
                arr1[ym][xm] = 2
                q.append([ym, xm])
    # 생존칸 찾기
    liveCnt = 0
    for i in arr1:
        for j in i:
            if j == 0:
                liveCnt += 1
    # 최대값 찾기
    if liveCnt > mx:
        mx = liveCnt
print(mx)
