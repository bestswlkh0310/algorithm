I=lambda:[*map(int,input().split())]
n = I()[0]
lst = [i for i in enumerate(I())]
idx = 0
for i in range(n - 1):
    print(end=f"{lst[idx][0] + 1} ")
    v = lst[idx][1]
    del lst[idx]
    bIdx = idx
    idx = (idx + v) % len(lst)
    if v >= 0 :
        idx -= 1

print(end=f"{lst[idx][0] + 1} ")

