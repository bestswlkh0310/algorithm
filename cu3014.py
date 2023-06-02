n = int(input())
arr = [0] * 100_001
lst = map(int, input().split())
for i in lst:
    arr[i] += 1

for (idx, i) in enumerate(arr):
    for j in range(i):
        print(end=f"{idx} ")