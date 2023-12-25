import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

arr = []
for _ in range(n):
    m, a, b, c = input().split()
    a = int(a)
    b = int(b)
    c = int(c)
    arr.append((m, a, b, c))

arr = list(sorted(arr, key=lambda x: (-x[1], x[2], -x[3], x[0])))
for i in arr:
    print(f"{i[0]}\n")