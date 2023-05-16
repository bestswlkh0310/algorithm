start, end = map(int, input().split())
s = [0] * end
i = 0
idx = 0
w = 1
iw = 1
while idx < end:
    s[idx] += w
    iw += 1
    if iw > w:
        w = iw
        iw = 1
    idx += 1
result = 0
for a in range(start - 1, end):
    result += s[a]
print(result)