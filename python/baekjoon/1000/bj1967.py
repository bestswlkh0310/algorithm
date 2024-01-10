import sys

sys.setrecursionlimit(10 ** 5)

n = int(input())
t = [[] for _ in range(n)]

for _ in range(n - 1):
    p, c, w = map(int, input().split())
    t[p - 1].append((c - 1, w))

r = []

def dfs(x):

    # 리프노드일 때
    if not len(t[x[0]]):
        # print(x[1])
        return (x[1], 0)

    chldLst = [dfs(i)[0] for i in t[x[0]]]
    if len(chldLst) == 1:
        r.append(chldLst[0])
    elif len(chldLst) >= 2:
        r.append(sum([*sorted(chldLst)][-2:]))
    bstChld = max(chldLst)
    # print(bstChld + x[1])
    return (bstChld + x[1], x[1])
    

for i in t[0]:
    dfs((0, i[1]))

if n == 1:
    print(0)
else:
    print(max(r))