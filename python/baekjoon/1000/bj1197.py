import sys
input = sys.stdin.readline
v, e = map(int, input().split())
parent = [i for i in range(v)]

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

class Edge:
    def __init__(self, a, b, w):
        self.node = [a, b]
        self.w = w

v = []
for _ in range(e):
    a, b, c = map(int, input().split())
    v.append(Edge(a - 1, b - 1, c))

v = [*sorted(v, key=lambda x: x.w)]
s = 0
for i in v:
    if not find_parent(i.node[0], i.node[1]):
        union_parent(i.node[0], i.node[1])
        s += i.w
print(s)