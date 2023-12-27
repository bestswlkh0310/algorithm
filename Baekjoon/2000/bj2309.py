arr = []
for i in range(9):
    arr.append(int(input()))
ls = []
sum = sum(arr)
for i in arr:
    for j in arr:
        if i == j: continue
        for k in arr:
            if k == j or k == i: continue
            for l in arr:
                if l == k or l == j or l == i: continue
                for h in arr:
                    if h == l or h == k or h == j or j == i: continue
                    for f in arr:
                        if f == h or f == k or f == j or f == i or f == l: continue
                        for g in arr:
                            if g == f or g == k or g == h or g == j or g == i or j == l: continue
                            if i + j + k + l + h + f + g == 100:
                                ls = [i, j, k, l, h, f, g]
ls.sort()
for i in ls:
    print(i)