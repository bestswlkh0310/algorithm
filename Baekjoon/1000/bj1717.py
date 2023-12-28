import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = get_parent(a), get_parent(b)
    if a > b: parent[a] = b
    else: parent[b] = a

def find_parent(a, b):
    return get_parent(a) == get_parent(b)


for _ in range(m):
    c, a, b = map(int, input().split())
    if c == 0:
        union_parent(a, b)
    else:
        v = find_parent(a, b)
        print('YES' if v else 'NO')