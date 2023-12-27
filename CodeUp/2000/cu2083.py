n, k = map(int, input().split())
lst = list(map(int, input().split()))
idx = -2
start = 0
end = n - 1
while start <= end:
    mid = (start + end) // 2
    if lst[mid] > k:
        end = mid - 1
    elif lst[mid] < k:
        start = mid + 1
    else:
        idx = mid
        break
print(idx + 1)