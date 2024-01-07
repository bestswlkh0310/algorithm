n=int(input())
a=[[*map(float,input().split())]for _ in range(n)]
class Edge:
    def __init__(self, a, b, w):
        self.node=[a,b]
        self.w=w
    def __str__(self):
        return f'Edge: node-{self.node} d-{self.w}'
def distance(n1,n2):
    return((n1[0]-n2[0])**2+(n1[1]-n2[1])**2)**0.5
parent=[i for i in range(n)]
def get_parent(x):
    if parent[x]==x:return x
    parent[x]=get_parent(parent[x])
    return parent[x]
def union_parent(a,b):
    a,b=get_parent(a),get_parent(b)
    parent[max(a,b)]=min(a,b)
def find_parent(a,b):
    return get_parent(a)==get_parent(b)
g=[]
for i in range(n):
    for j in range(i, n):
        if i == j: continue
        n1=a[i]
        n2=a[j]
        g.append(Edge(i,j,distance(n1,n2)))
g=[*sorted(g,key=lambda x:x.w)]
s=0
for i in g:
    if not find_parent(i.node[0],i.node[1]):
        union_parent(i.node[0],i.node[1])
        s+=i.w
print(s)
