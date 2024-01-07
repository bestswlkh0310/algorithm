import sys
import collections

m, n, o, p, q, r, s, t, u, v, w = map(int, sys.stdin.readline().split())
arr = [[[[[[[[[[0 for _ in range(n)] for _ in range(o)] for _ in range(p)] for _ in range(q)] for _ in range(r)] for i in range(s)] for _ in range(t)] for _ in range(u)] for _ in range(v)] for _ in range(w)]
qu = collections.deque()
cnt = 0
for i in range(w):
    for j in range(v):
        for k in range(u):
            for l in range(t):
                for a in range(s):
                    for b in range(r):
                        for x in range(q):
                            for y in range(p):
                                for z in range(o):
                                    for e in range(n):
                                        lst = (list(map(int, sys.stdin.readline().split())))
                                        for (idx, qq) in enumerate(lst):
                                            if qq == 0:
                                                cnt += 1
                                            if qq == 1:
                                                qu.append((i,j,k,l,a,b,x,y,z,e,idx, 1))
                                        arr[i][j][k][l][a][b][x][y][z][e] = lst
dd = (
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1),
    (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1),
)

mx = 0
cnt1 = 0

while qu:
    pop = qu.popleft()
    a = pop[0]
    b = pop[1]
    c = pop[2]
    d = pop[3]
    e = pop[4]
    f = pop[5]
    g = pop[6]
    h = pop[7]
    i = pop[8]
    j = pop[9]
    k = pop[10]
    n1 = pop[11]
    for k1 in dd:
        a1 = a + k1[0]
        b1 = b + k1[1]
        c1 = c + k1[2]
        d1 = d + k1[3]
        e1 = e + k1[4]
        f1 = f + k1[5]
        g1 = g + k1[6]
        h1 = h + k1[7]
        i1 = i + k1[8]
        j1 = j + k1[9]
        k0 = k + k1[10]
        if 0 <= a1 < w and 0 <= b1 < v and 0 <= c1 < u and 0 <= d1 < t and 0 <= e1 < s and 0 <= f1 < r and 0 <= g1 < q and 0 <= h1 < p and 0 <= i1 < o and 0 <= j1 < n and 0 <= k0 < m and not arr[a1][b1][c1][d1][e1][f1][g1][h1][i1][j1][k0]:
            cnt1 += 1
            arr[a1][b1][c1][d1][e1][f1][g1][h1][i1][j1][k0] = n1
            if n1 > mx: mx = n1
            qu.append((a1, b1, c1, d1, e1, f1, g1, h1, i1, j1, k0, n1 + 1))
if not cnt:
    print(0)
elif cnt == cnt1:
    print(mx)
else:
    print(-1)
