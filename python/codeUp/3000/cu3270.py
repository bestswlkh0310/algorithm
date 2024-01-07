n, m = map(int, input().split())
parent = [i for i in range(n)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)
    if a > b: parent[a] = b
    else: parent[b] = a

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a - 1, b - 1)

for i in range(n):
    print(get_parent(i) + 1)