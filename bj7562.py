import collections

for k in range(int(input())):
    wh = int(input())

    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())

    if x1 == x2 and y1 == y2:
        print(0)
        continue

    lst = [[0 for i in range(wh)] for i in range(wh)]

    dxy = ((2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1))

    q = collections.deque()
    q.append((y1, x1, 1))

    while q:
        (y, x, n) = q.popleft()
        for i in dxy:
            xw = x + i[0]
            yw = y + i[1]
            if 0 <= xw < wh and 0 <= yw < wh and lst[yw][xw] == 0:
                lst[yw][xw] = n
                q.append((yw, xw, n + 1))

    print(lst[y2][x2])
