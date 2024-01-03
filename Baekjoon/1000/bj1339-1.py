n = int(input())
arr = [list(input()) for _ in range(n)]
mxLen = max([len(i) for i in arr])
d = [None for _ in range(26)]
idx = 9
for i in range(mxLen):
    jArr = [*sorted([(j[i - (mxLen - len(j))], sum([k.count(j[i - (mxLen - len(j))]) for k in arr])) for j in arr if len(j) >= mxLen - i and d[ord(j[i - (mxLen - len(j))]) - ord('A')] == None], key=lambda x: -x[1])]
    for j in jArr:
        if d[ord(j[0]) - ord('A')] == None:
            d[ord(j[0]) - ord('A')] = idx
            idx -= 1
print(d)
print(sum(map(int, [''.join(map(str, [d[ord(j[0]) - ord('A')] for j in i])) for (idx, i) in enumerate(arr)])))
# 2
# GCF
# ACDEB



# AAB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
