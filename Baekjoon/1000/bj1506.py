import sys
sys.setrecursionlimit(10**5)
I=input

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

    N=int(I())
    d = [0 for _ in range(N)]
    v = [False for _ in range(N)]
    SCC = []
    s = []
    id = 0
    C=[*map(int, I().split())]
    L=[[*map(int, list(str(I())))] for _ in range(N)]
    A=[[]for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if L[i][j] == 1:
                A[i].append(j)

    for i in range(N):
        if d[i] == 0:
            dfs(i)
    s = 0
    for i in SCC:
        s += min([C[j - 1] for j in i])
    print(s)