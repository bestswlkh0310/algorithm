import sys

input = sys.stdin.readline

n = int(input())
arr = [*sorted([int(input()) for _ in range(n)])]

r = 0

for i in range(n - 1):
    arr[1] += arr[0]
    # print(f'v - {arr[i + 1]}')
    r += arr[1]
    arr.pop(0)
    arr.sort()

# print(sum(arr))
print(r)
