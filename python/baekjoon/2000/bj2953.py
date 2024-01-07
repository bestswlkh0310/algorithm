mxIdx = 0
mxVal = 0
for i in range(5):
    s = sum(list(map(int, input().split())))
    if mxVal < s:
        mxVal = s
        mxIdx = i + 1
print(mxIdx, mxVal)