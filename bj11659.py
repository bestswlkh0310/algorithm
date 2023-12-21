import sys

n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    sys.stdout.write(f"{sum(lst[a - 1:b])}\n")
