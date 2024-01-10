from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()
g = [[] for _ in range(n)]
v = [False for _ in range(n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    g[a-1].append(b-1)
    g[b-1].append(a-1)

q = deque([(0, 1)])
v[0] = True
result = [s[0]]
lst = [0]

while q:
    x, cnt = q.popleft()
    l = []
    for i in g[x]:
        if not v[i]:
            v[i] = True
            l.append(i)

    l = [*sorted(l, key=lambda x: -ord(s[x]))]

    if not l: continue
    k = l[0]
    l = [(i, cnt + 1) for i in l if s[k] == s[i]]
    if len(result) == cnt:
        if x in lst:
            result.append(s[k])
            lst = [c[0] for c in l]
        else:
            continue
    else:
        if result[cnt] < s[k]:
            result[cnt] = s[k]
            lst = [c[0] for c in l]
        elif result[cnt] == s[k]:
            lst.append(k)
        else:
            continue
    q.extend(l)
    
print(''.join([i[0] for i in result]))

# 반례:d
# 6
# abbcdc
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# abd

# 5
# abbcd
# 1 2
# 1 3
# 3 5
# 2 4
# abd

# 8
# dfcjsasb
# 8 4
# 6 3
# 1 3
# 2 1
# 4 1
# 4 7
# 2 5
# djs

# 7
# aaaaaaa
# 1 2
# 1 3
# 3 4
# 3 5
# 5 6
# 5 7
# aaaa

# 7
# abbcddc
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 7
# abdc

# 9
# abbcdccab
# 1 2
# 1 3
# 2 4
# 3 5
# 4 6
# 5 7
# 7 8
# 6 9
# abdca
