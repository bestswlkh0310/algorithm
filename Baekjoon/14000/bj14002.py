_ = int(input())
lst = list(map(int, input().split()))

arr = [1001 for i in range(1000)]

for i in lst:
    for (idx, j) in enumerate(arr):
        if j > i:
            arr[idx] = i
            break
        elif i == j:
            break

ar = [i for i in arr if i != 1001]

print(len(ar))

print(' '.join(map(str, ar)))
