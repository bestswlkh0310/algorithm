import sys
n = int(input())
lst = list(map(int, sys.stdin.readline().split()))
n1 = int(input())
lst1 = list(map(int, sys.stdin.readline().split()))
for i in lst1:
    sys.stdout.write(f"{int(i in lst)} ")