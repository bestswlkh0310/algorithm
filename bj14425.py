a, b = map(int, input().split())

arr = []
cnt = 0

for _ in range(a):
    arr.append(input())

for _ in range(b):
    if input() in arr:
        cnt += 1


print(cnt)