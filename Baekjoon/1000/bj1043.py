import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


n, m = map(int, input().split())

t = [*map(int, input().split())]
del t[0]
parent = [i for i in range(n + m)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x] 

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

for i in range(m): # 파티
    m1 = [*map(int, input().split())]
    del m1[0]
    for j in m1: # 참석자들
        union_parent(i, j + m - 1)
# print(parent)
for i in t:
    v = get_parent(i - 1 + m)
    for j in range(m):
        if parent[j] == v:
            print(j)
            # parent[j] = -1
print(parent)
print(parent[:m])

print(len([0 for i in parent[:m] if i != -1]))
