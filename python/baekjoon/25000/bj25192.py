import sys

input = sys.stdin.readline

n = int(input())

arr = []
cnt = 0
for _ in range(n):
    str = input().strip()
    if str == 'ENTER':
        cnt += len(set(arr))
        arr = []
    else:
        arr.append(str)

print(cnt + len(set(arr)))