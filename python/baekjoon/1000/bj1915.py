n, m = map(int, input().split())
g = [[*map(int, list(input()))] for _ in range(n)]
v = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    for j in range(m):
        if g[i][j]:
            v[i][j] = 1
        if i > 0 and j > 0 and g[i][j] and g[i - 1][j] and g[i][j - 1]:
            v[i][j] = min(v[i - 1][j - 1], v[i - 1][j], v[i][j - 1]) + 1
        #     print(min(v[i - 1][j - 1], g[i - 1][j], g[i][j - 1]))
        # print('----------')
        # for k in v:
        #     print(k)

print(max([max(i) for i in v]) ** 2)
# 3 1
# 0
# 1
# 1

# 5 5
# 11100
# 11110
# 11111
# 01111
# 00111