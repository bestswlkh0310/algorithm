n, m = map(int, input().split())

parent = [i for i in range(n)]

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

    def __str__(self):
        return f'{self.node} {self.w}'

def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

edges = []
d = []

for _ in range(n):
    a, b = map(int, input().split())
    d.append((a - 1, b - 1))

for i in range(n):
    for j in range(i + 1):
        if i == j: continue
        edges.append(Edge(i, j, distance(d[i][0], d[i][1], d[j][0], d[j][1])))

for _ in range(m):
    a, b = map(int, input().split())
    union_parent(a - 1, b - 1)
    n1, n2 = d[a - 1], d[b - 1]

edges = [*sorted(edges, key=lambda x: x.w)]

s = 0
for i in edges:
    if not find_parent(i.node[0], i.node[1]):
        union_parent(i.node[0], i.node[1])
        s += i.w

print('{:.2f}'.format(s, 2))