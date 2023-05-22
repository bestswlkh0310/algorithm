n = int(input())
lst = list(map(int, input().split()))
k = int(input())
arr = [False] * 1_000_001
for i in lst:
    arr[i] = True
cnt = 0
for i in lst:
    if 1 <= k - i <= 1_000_000 and arr[k - i]:
        cnt += 1
print(cnt // 2)