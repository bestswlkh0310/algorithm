import sys
a, b = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 1
t = True
result = -1
for i in range(a - 1):
    if t:
        for j in range(a - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                if cnt == b:
                    result = (lst[j], lst[j + 1])
                    t = False
                    break
                cnt += 1
if result == -1:
    sys.stdout.write(f"{result}")
else:
    for i in sorted(result):
        sys.stdout.write(f"{i} ")