import sys
h, w, t = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))
air = []
for _ in range(t):
    stack = [[0] * w for _ in range(h)]

    for i in range(h):
        for j in range(w):
            if arr[i][j] == -1:
                air.append(i)
                continue
            cnt = 0
            for k in dxy:
                y1 = i + k[1]
                x1 = j + k[0]
                if 0 <= x1 < w and 0 <= y1 < h:
                    stack[y1][x1] += arr[i][j] // 5
                    if arr[y1][x1] != -1:
                        cnt += 1
            arr[i][j] -= arr[i][j] // 5 * cnt
    for i in range(h):
        for j in range(w):
            if arr[i][j] == -1: continue
            arr[i][j] += stack[i][j]
    # 순회
    for i in range(air[0] - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    for i in range(w - 1):
        arr[0][i] = arr[0][i + 1]
    for i in range(air[0]):
        arr[i][-1] = arr[i + 1][-1]
    for i in range(w - 1, 1, -1):
        arr[air[0]][i] = arr[air[0]][i - 1]
        if i == 2: arr[air[0]][i - 1] = 0
    # 아래 순회
    for i in range(air[1] + 1, h - 1):
        arr[i][0] = arr[i + 1][0]
    for i in range(w - 1):
        arr[h - 1][i] = arr[h - 1][i + 1]
    for i in range(h - 1, air[1], -1):
        arr[i][-1] = arr[i - 1][-1]
    for i in range(w - 1, 0, -1):
        arr[air[1]][i] = arr[air[1]][i - 1]
        if i == 1: arr[air[1]][i] = 0

    # for i in arr:
    #     print(i)
    # print()
# print()
# 7 8 1
# 0 0 0 0 0 0 0 9
# 0 0 0 0 3 0 0 8
# -1 0 5 0 0 0 22 0
# -1 8 0 0 0 0 0 0
# 0 0 0 0 0 10 43 0
# 0 0 5 0 15 0 0 0
# 0 0 40 0 0 0 20 0

result = 0
for i in arr:
    result += sum(i)
print(result + 2)
