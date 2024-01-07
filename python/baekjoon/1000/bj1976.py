import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

parent = [i for i in range(n)]

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


for i in range(n):
    for (idx, j) in enumerate([*map(int, input().split())]):
        if j == 1:
            union_parent(i, idx)

travel = [*map(int, input().split())]
for i in range(m - 1):
    if not find_parent(travel[i] - 1, travel[i + 1] - 1):
        print('NO')
        exit(0)

print('YES')