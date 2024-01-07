import sys
import math
input = sys.stdin.readline
n = int(input())

arr = [[*map(int, input().split())] for _ in range(n)]
arr1 = [[None for _ in range(n // 2)] for _ in range(n // 2)]

for _ in range(int(math.log(n, 2))):
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            v = [*sorted([arr[i][j], arr[i + 1][j], arr[i][j + 1], arr[i + 1][j + 1]])]
            arr1[i // 2][j // 2] = v[-2]
    arr = arr1
    n //= 2
    arr1 = [[None for _ in range(n // 2)] for _ in range(n // 2)]
print(arr[0][0])
