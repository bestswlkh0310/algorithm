n, m = map(int, input().split())
lst = [*sorted([*map(int, input().split())])]
result = []

def A(v, r):
    global n
    if len(r) == m:
        result.append(' '.join([*map(str, r)]))
        return
    for (idx, i) in enumerate(v):
        newV = v[:]
        newR = r[:]
        newR.append(newV[idx])
        A(newV[idx:], newR)

A(lst, [])

dic = {}

for i in result:
    if i not in dic:
        dic[i] = 1
        print(i)