import sys
input = sys.stdin.readline
n, e = map(int, input().split())
sys.setrecursionlimit(10**5)

A = [[] for _ in range(n)]
d = [0 for _ in range(n)]
v = [False for _ in range(n)]
SCC = []
s = []
id = 0

def dfs(x):
    global id
    id += 1
    d[x] = id
    s.append(x)

    parent = id

    for i in A[x]:
        if d[i] == 0:
            parent = min(parent, dfs(i))
        elif not v[i]:
            parent = min(parent, d[i])
    
    if d[x] == parent:
        scc = []
        while True:
            t = s.pop()
            scc.append(t + 1)
            v[t] = True
            if t == x:
                break
        SCC.append(scc)


    return parent

if __name__ == '__main__':
    for i in range(e):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        A[a].append(b)
    for i in range(n):
        if d[i] == 0:
            dfs(i)
    print(len(SCC))
    SCC = [*sorted([sorted(i) for i in SCC], key=lambda x: x[0])]

    for i in SCC:
        print(' '.join([*map(str, i)]) + ' -1')
        