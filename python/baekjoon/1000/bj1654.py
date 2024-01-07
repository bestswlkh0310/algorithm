k, n = map(int, input().split())
arr = [0] * k
mx = -1
for i in range(k):
    arr[i] = int(input())
    if mx < arr[i]:
        mx = arr[i]

result = 0
start = 0
end = mx
while start <= end:
    mid = (start + end + 1) // 2
    s = 0
    for i in arr:
        s += i // mid
    if s >= n:
        start = mid + 1
        result = mid
    elif s < n:
        end = mid - 1
print(result)

# 5 10
# 1
# 100
# 100
# 100
# 100
#
# 1 1
# 112312312312