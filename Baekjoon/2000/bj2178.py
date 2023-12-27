h, w = map(int, input().split())
arr = []
for i in range(h):
    arr.append(list(map(int, list(input()))))
q = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
q.append([0, 0, 2])
while len(q) != 0:
    xy = q[0]
    x = xy[0]
    y = xy[1]
    n = xy[2]
    del q[0]
    for i in range(4):
        x1 = x + dx[i]
        y1 = y + dy[i]
        if 0 <= x1 < w and 0 <= y1 < h and arr[y1][x1] == 1:
            arr[y1][x1] = n
            q.append([x1, y1, n + 1])
arr[0][0] = 1

print(arr[-1][-1])