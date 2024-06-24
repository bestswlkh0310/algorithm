import sys

D = [1, 2, 4, 7]

for i in range(1_000_000):
    D.append((D[-1] * 2 - D[-4]) % 1_000_000_009)

for _ in range(int(input())):
    n = int(input())
    print(D[n - 1])