from collections import deque
import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

dxy = ((1, 0), (-1, 0), (0, 1), (0, -1))

q = deque()
q.append((0, 0))
arr[0][0] = -1

t = True
cnt = 0

while t:
    while q:
        (x, y) = q.popleft()
        for (dx, dy) in dxy:
            x1 = x + dx
            y1 = y + dy
            if 0 <= x1 < m and 0 <= y1 < n:
                if arr[y1][x1] == 0:
                    arr[y1][x1] = -1
                    q.append((x1, y1))
                elif arr[y1][x1] > 0:
                    arr[y1][x1] += 1
    # print(f"---------{cnt}\n")
    # for i in arr:
    #     for j in i:
    #         print("%2s " % (j))
    #     print('\n')
    t1 = False
    for i in range(n):
        for j in range(m):
            if arr[i][j] == -1:
                arr[i][j] = 0
            elif arr[i][j] >= 3:
                arr[i][j] = 0
                t1 = True
            elif arr[i][j] == 2:
                arr[i][j] = 1
    if not t1:
        t = False
        break
    cnt += 1
    q.append((0, 0))
    arr[0][0] = -1
print(f"{cnt}")

# 3 3
# 0 0 0
# 0 1 0
# 0 0 0

# 8 9
# 0 0 0 0 0 0 0 0 0
# 0 0 0 1 1 0 0 0 0
# 0 0 0 1 1 0 1 1 0
# 0 0 1 1 1 1 1 1 0
# 0 0 1 1 1 1 1 0 0
# 0 0 1 1 0 1 1 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0

# 3 3
# 0 0 0
# 0 1 0
# 0 0 0

# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 2 2 0 0 0 0
# 0 0 0 1 1 1 2 0 0
# 0 0 2 1 1 1 2 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0
# 0 0 0 0 0 0 0 0 0