s1 = input()
s2 = input()
s3 = input()
l = len(s1)
l2 = len(s2)
l3 = len(s3)

g = [[[0 for _ in range(l3 + 1)] for _ in range(l2 + 1)] for _ in range(l + 1)]

for i in range(l):
    for j in range(l2):
        for k in range(l3):
            if s1[i] == s2[j] == s3[k]:
                g[i + 1][j + 1][k + 1] = g[i][j][k] + 1
            else:
                g[i + 1][j + 1][k + 1] = max(g[i + 1][j + 1][k], g[i][j + 1][k + 1], g[i + 1][j][k + 1])

print(g[-1][-1][-1])