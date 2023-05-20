h, w = map(int, input().split())
y, x, d = map(int, input().split())

arr = [list(map(int, input().split())) for i in range(h)]

dxy = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt = 0
while True:
    if arr[y][x] == 0:
        arr[y][x] = 2
        cnt += 1

    isDoneClean = True
    for i in dxy:
        mx = x + i[0]
        my = y + i[1]
        if 0 <= mx < w and 0 <= my < h and arr[my][mx] == 0:
            isDoneClean = False
    if isDoneClean:
        mx = x + dxy[(d + 2) % 4][1]
        my = y + dxy[(d + 2) % 4][0]
        if 0 <= mx < w and 0 <= my < h and arr[my][mx] != 1:
            x = mx
            y = my
        else:
            break
    else:
        d = (d + 3) % 4
        mx = x + dxy[d][1]
        my = y + dxy[d][0]
        if 0 <= mx < w and 0 <= my < h and arr[my][mx] == 0:
            x = mx
            y = my
print(cnt)