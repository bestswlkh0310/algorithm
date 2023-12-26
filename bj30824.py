import sys

input = sys.stdin.readline
print = sys.stdout.write

arr = [1, 1]
while arr[-1] <= 10**16:
    arr.append(arr[-1] + arr[-2])

del arr[-1]

for _ in range(int(input())):
    k, x = map(int, input().split())
    t = False
    if k == 1:
        t = x in arr
    elif k == 2:
        for i in arr:
            for j in arr:
                if i + j == x:
                    t = True
                    break
    elif k == 3:
        for i in arr:
            for j in arr:
                for l in arr:
                    if i + j + l == x:
                        t = True
                        break

    if t:
        print('YES\n')
    else:
        print('NO\n')