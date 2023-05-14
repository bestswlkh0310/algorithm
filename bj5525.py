import sys
n = int(sys.stdin.readline())
s = "IOI" + "OI" * (n - 1)
cnt = 0
length = int(sys.stdin.readline())
inp = sys.stdin.readline()
for i in range(length - len(s) + 1):
    if s == inp[i:i + len(s)]:
        cnt += 1
print(cnt)