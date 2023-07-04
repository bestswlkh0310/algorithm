n = int(input())
lst = [int(input()) for _ in range(n)]
mx = -1
for i in range(1, n + 1):
    s = 0
    for j in lst:
        if j * i > mx:
            s += j * i
