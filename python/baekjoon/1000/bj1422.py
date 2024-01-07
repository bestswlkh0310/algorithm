k, n = map(int, input().split())

lst = [int(input()) for _ in range(k)]

mxL = n - k + 1
mx = 0

# r: 결과, i: 개수
def go(r, visit, i, mxL):
    global mx
    if i == n:
        l = int(''.join(map(str, r)))
        l2 = int(''.join(reversed(list(map(str, r)))))
        print(l)
        print(l2)
        if mx < l:
            mx = l
        if mx < l2:
            mx = l2
        return
    
    # handling
    for v in range(len(visit)):
        if visit[v] < mxL:
            newVisit = visit[:]
            newR = r[:]

            newVisit[v] += 1
            newR.append(lst[v])

            if newVisit[v] == mxL:
                mxL = 1
            go(newR, newVisit, i + 1, mxL)
    

visit = [0 for _ in range(k)]

for (idx, k) in enumerate(lst):
    nv = visit[:]
    nv[idx] += 1
    go([k], nv, 1, mxL)

print(mx)