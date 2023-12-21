_ = int(input())
lst = list(map(int, input().split()))

arr = [0 for _ in range(1001)]

for i in lst:
    
    v = i + max(arr[0:i])
    # for j in range(i - 1, 0, -1):
    #     if arr[j] != -1:
    #         v += arr[j]
    #         break
    arr[i] = v
print(max([i for i in arr if i != -1]))

