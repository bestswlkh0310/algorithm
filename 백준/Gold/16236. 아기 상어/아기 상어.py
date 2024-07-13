from collections import deque as Q

I=input
N=int(I())
G=[[*map(int, I().split())]for _ in range(N)]
Y,X=0,0
for i in range(N):
    for j in range(N):
        if G[i][j] == 9:
            Y,X=i,j

dxy = ((-1,0),(1,0),(0,-1),(0,1))
# dxy = ((-1,0),(0,1),(0,-1),(1,0))
level = 2
point = 0

def bfs():
    q = Q([(Y,X,0,-1)])
    v = [[False] * N for _ in range(N)]
    v[Y][X] = True
    r = []
    while q:
        y,x,cnt,d=q.popleft()
        for idx, (dy,dx) in enumerate(dxy):
            y1=y+dy
            x1=x+dx
            if 0 <= y1 < N and 0 <= x1 < N and not v[y1][x1]:
                d1 = idx if cnt == 0 else d
                v[y1][x1] = True
                if G[y1][x1] < level and G[y1][x1] != 0: # can eat
                    r.append((y1, x1, cnt+1, d1))
                elif G[y1][x1] == level or G[y1][x1] == 0:
                    q.append((y1,x1,cnt+1,d1))
    if len(r) == 0:
        return -1
    r.sort(key=lambda x: (x[2], x[0], x[3]))
    # print(r)
    return r[0]

t = 0

while True:
    R = bfs()
    if R == -1:
        print(t)
        # print('끝!')
        break
    y1, x1, cnt,_ = R
    t += cnt
    G[Y][X] = 0
    Y = y1
    X = x1
    if G[Y][X] < level and G[Y][X] != 0:
        point += 1
    G[Y][X] = 9
    if point == level:
        level += 1
        point = 0

    # print()
    # print(t, point, level)
    # for i in G:
    #     print(i)

