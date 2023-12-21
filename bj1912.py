n = int(input())
lst = list(map(int, input().split()))

mx = -1001
lMx = -1001

for i in lst:
    mx = max(mx + i, i)
    if mx > lMx:
        lMx = mx

print(lMx)