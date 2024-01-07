import sys

input = sys.stdin.readline
print = sys.stdout.write

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
s = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        s[i + 1][j + 1] = s[i + 1][j] + s[i][j + 1] + arr[i][j] - s[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(f"{s[x2][y2] + s[x1 - 1][y1 - 1] - s[x2][y1 - 1] - s[x1 - 1][y2]}\n")