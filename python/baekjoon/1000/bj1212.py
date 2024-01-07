# print(str(bin(int(str(int(input())), 8)))[2:])

import sys

n = int(input())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort()
for i in range(n):
    sys.stdout.write(f"{arr[i]}\n")
