import sys
n, c = map(int, input().split())
arr = sorted([int(sys.stdin.readline()) for i in range(n)])
start = 1
result = 0
end = arr[-1] - arr[0]
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    s = 0
    for i in range(n):
        if arr[i] - arr[s] >= mid:
            cnt += 1
            s = i
    if cnt >= c:
        start = mid + 1
    else:
        end = mid - 1
print((start + end) // 2)
