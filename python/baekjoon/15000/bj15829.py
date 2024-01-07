n = int(input())
print("%d" %(sum([j * (31 ** i) for (i, j) in enumerate([ord(i) - ord('a') + 1 for i in list(input())])]) // 1 % 1234567891))
