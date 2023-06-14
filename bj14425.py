import sys
a, b = map(int, input().split())

arr = [sys.stdin.readline() for _ in range(a)]
cnt = 0
for _ in range(b):
    inp = sys.stdin.readline()
    t = False
    for s in arr:
        if inp in s:
            t = True
            break
    if t:
        cnt += 1

print(cnt)