from collections import deque as D
a,b,c=map(int,input().split())
r=[]
dic={}
q=D([(0,0,c)])
while q:
    (a1,b1,c1)=q.popleft()
    f=f'{a1} {b1} {c1}'
    if f in dic:
        continue
    else:
        dic[f]=False
    if c1 not in r and a1 == 0:
        r.append(c1)
    if a1<a:
        v=a-a1
        if v<=b1:
            q.append((a,b1-v,c1))
        else:
            q.append((a1+b1,0,c1)) # [1:10,3:10]
        if v<=c1:
            q.append((a,b1,c1-v))
        else:
            q.append((a1+c1,b1,0))
    if b1<b:
        v=b-b1
        if v<=a1:
            q.append((a1-v,b,c1))
        else:
            q.append((0,b1+a1,c1))
        if v<=c1:
            q.append((a1,b,c1-v))
        else:
            q.append((a1,b1+c1,0))
    if c1<c:
        v=c-c1
        if v<=a1:
            q.append((a1-v,b1,c))
        else:
            q.append((0,b1,c1+a1))
        if v<=b1:
            q.append((a1,b1-v,c))
        else:
            q.append((a1,0,c1+b1))

for i in[*sorted(r)]:
    print(end=f'{i} ')