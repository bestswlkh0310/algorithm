n = int(input())
arr = list(map(int, input().split()))
arr.append(0)
k = 0
s = 0
for i in range(n):
    if not arr[i]: continue
    if arr[i] != arr[i + 1]:
        k = 1
        s += k
    else:
        if k == 0:
            k = 1
        k += 1
        s += k
print(s)