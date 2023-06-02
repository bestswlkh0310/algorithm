a, b = map(int, input().split())
l = 10 ** 7
arr = [True] * l
arr[0] = arr[1] = False
cnt = 0
for (idx, k) in enumerate(arr):
    if k:
        s = idx * 2
        while s < l:
            arr[s] = False
            s += idx
        i = 2
        s = idx ** i
        while s <= 10 ** 14:
            if a <= s <= b:
                cnt += 1
            i += 1
            s = idx ** i
print(cnt)
# 10000000000000 100000000000000