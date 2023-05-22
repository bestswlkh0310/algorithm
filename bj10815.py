import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
arr = [False] * 20_000_001
for i in lst:
    arr[i + 10_000_000] = True

n1 = int(input())
lst1 = list(map(int, sys.stdin.readline().split()))
for i in lst1:
    print(end=f"{int(arr[i + 10_000_000])} ")