wh = int(input())
arr = []
for i in range(wh):
    arr.append(list(map(int, list(input()))))

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def find(x, y):
    cnt = 1
    q = [[x, y]]
    while len(q) != 0:
        xy = q[0]
        del q[0]
        x1 = xy[0]
        y1 = xy[1]
        for i in range(4):
            xm = x1 + dx[i]
            ym = y1 + dy[i]
            if 0 <= xm < wh and 0 <= ym < wh and arr[ym][xm] == 1:
                arr[ym][xm] = 0
                cnt += 1
                q.append([xm, ym])
    return cnt

result = []
cnt = 0
for i in range(wh):
    for j in range(wh):
        if arr[i][j] == 1:
            arr[i][j] = 0
            result.append(find(j, i))
            cnt += 1
print(cnt)
for i in sorted(result):
    print(i)