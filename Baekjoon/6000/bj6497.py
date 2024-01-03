import sys
input = sys.stdin.readline
def get_parent(x):
    if parent[x] == x: return parent[x]
    parent[x] = get_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a, b = get_parent(a), get_parent(b)
    parent[max(a, b)] = min(a, b)

def find_parent(a, b):
    return get_parent(a) == get_parent(b)

class Edge:
    def __init__(self, a, b, w):
        self.node = [a, b]
        self.w = w
r = []

while True:
    m, n = map(int, input().split())

    if m + n == 0: break

    parent = [i for i in range(m)]
    edges = []
    s1 = 0
    for _ in range(n):
        a, b, w = map(int, input().split())
        edges.append(Edge(a, b, w))
        s1 += w

    edges = [*sorted(edges, key=lambda x: x.w)]
    s = 0

    for i in edges:
        if not find_parent(i.node[0], i.node[1]):
            union_parent(i.node[0], i.node[1])
            s += i.w
    r.append(s1 - s)


for i in r:
    print(i)