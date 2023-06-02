import random
import sys

n = int(input())
arr = [[False] * n for i in range(n)]
r = n / 2

for i in range(10000):
    y, x = random.randint(0, n - 1), random.randint(0, n - 1)
    if not arr[y][x]:
        arr[y][x] = True
        for i in arr:
            for j in i:
                sys.stdout.write("*" if j else "_")
            sys.stdout.write("\n")
        sys.stdout.write("----------------------------------------\n")