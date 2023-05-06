import sys
import collections
h, w = map(int, sys.stdin.readline().split())
cnt = 0
arr = []
q = collections.deque()

dp = ((1, 0), (-1, 0), (0, 1), (0, -1))
r = 0
mx = 0


for i in range(h):
    arr.append(list(map(int, sys.stdin.readline().split())))

def show():
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()
    print("----------------")


def bfs():
    while q:
        global r
        (y, x) = q.popleft()
        for k in dp:
            dx = x + k[0]
            dy = y + k[1]
            if 0 <= dx < w and 0 <= dy < h and arr[dy][dx] == 1:
                arr[dy][dx] = 0
                q.append((dy, dx))
                r += 1


for i in range(h):
    for j in range(w):
        if arr[i][j] == 1:
            arr[i][j] = 0
            q.append((i, j))
            bfs()
            show()
            cnt += 1
            if r > mx:
                mx = r
            r = 0
print(cnt)
if cnt == 0:
    print(0)
else:
    print(mx + 1)