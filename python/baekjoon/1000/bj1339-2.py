n = int(input())
arr = [list(input()) for _ in range(n)]
mxLen = max([len(i) for i in arr])
d = [0 for _ in range(26)]

for i in arr:
    for (idx, j) in enumerate(i[::-1]):
        d[ord(j) - ord('A')] += 10 ** idx

idx = 9

for i in [*sorted([i for i in enumerate(d)], key=lambda x: x[1])][::-1]:
    d[i[0]] = idx
    idx -= 1

print(sum(map(int, [''.join(map(str, [d[ord(j[0]) - ord('A')] for j in i])) for (idx, i) in enumerate(arr)])))
