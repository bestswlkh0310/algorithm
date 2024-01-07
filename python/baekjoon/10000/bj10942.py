import sys
input = sys.stdin.readline
n = int(input())
lst = [*map(int, input().split())]
g = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(min(i + 1, n - i)):
        if lst[i + j] == lst[i - j]:
            g[i - j][i + j] = 1
        else:
            break
    j = 0
    i1 = i - 1
    j = 0
    while 0 <= i + j < n and 0 <= i1 - j < n:
        if lst[i + j] == lst[i1 - j]:
            g[i1 - j][i + j] = 1
            j += 1
        else:
            break

for _ in range(int(input())):
    a, b = map(int, input().split())
    print(g[a - 1][b - 1])
