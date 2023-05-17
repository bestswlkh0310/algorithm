import collections

for i in range(int(input())):
    w, h = map(int, input().split())
    arr = []
    visit = [[-1] * w for i in range(h)]
    visitS = [[-1] * w for i in range(h)]
    for i in range(h):
        arr.append(list(input()))
    pos = None
    fireQ = collections.deque()
    q = collections.deque()

    for i in range(h):
        for j in range(w):
            if arr[i][j] == '@':
                visitS[i][j] = 0
                q.append((i, j, 1))
            if arr[i][j] == '*':
                visit[i][j] = 0
                fireQ.append((i, j, 1))
    dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while fireQ:
        (fy, fx, n) = fireQ.popleft()
        for k in dxy:
            my = fy + k[0]
            mx = fx + k[1]
            if 0 <= mx < w and 0 <= my < h and visit[my][mx] == -1 and (arr[my][mx] == '.' or arr[my][mx] == '@'):
                visit[my][mx] = n
                fireQ.append((my, mx, n + 1))

    while q:
        (y, x, n) = q.popleft()
        for k in dxy:
            my = y + k[0]
            mx = x + k[1]
            if 0 <= mx < w and 0 <= my < h and visitS[my][mx] == -1 and (arr[my][mx] == '.'):
                visitS[my][mx] = n
                q.append((my, mx, n + 1))
    t = False
    reArr = [[False] * w for i in range(h)]
    mnArr = []
    for i in range(h):
        for j in range(w):
            if visitS[i][j] != -1 and visit[i][j] != - 1 and visit[i][j] > visitS[i][j] or (visitS[i][j] != -1 and visit[i][j] == -1):
                reArr[i][j] = True

    for i in range(h):
        if reArr[i][0]:
            mnArr.append(visitS[i][0])
            t = True
        if reArr[i][-1]:
            mnArr.append(visitS[i][-1])
            t = True
    for i in range(w):
        if reArr[0][i]:
            mnArr.append(visitS[0][i])
            t = True
        if reArr[-1][i]:
            mnArr.append(visitS[-1][i])
            t = True
    if t:
        print(min(mnArr) + 1)
    else:
        print("IMPOSSIBLE")