import sys

input = sys.stdin.readline

n, m = map(int, input().split())

parent = [i for i in range(n)]

def get_parent(x):
    if parent[x] == x: return x
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = get_parent(a), get_parent(b)
    parent[max(a, b)] = min(a, b)

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

for i in range(m):
    a, b = map(int, input().split())
    if not find_parent(a, b):
        union_parent(a, b)
    else:
        print(i + 1)
        exit(0)
print(0)