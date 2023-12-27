I = lambda: [*map(int, input().split())]
n, m = I()
lst = I()
v = [0 for i in range(n)]

for i in range(n):
    if lst[i] % m == 0:
        v[i] += 1
        if i > 0:
            v[i] += v[i - 1]
    elif i > 0 and (lst[i] + lst[i - 1]) % m == 0:
        v[i] += 1
        if i > 1:
            v[i] += v[i - 2]

print(v)