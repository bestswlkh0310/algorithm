import heapq
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())

l = []

for _ in range(n):
    k = int(input())
    if k == 0:
        if len(l) == 0:
            print('0\n')
        else:
            print(f"{heapq.heappop(l)}\n")
    else:
        heapq.heappush(l, k)

