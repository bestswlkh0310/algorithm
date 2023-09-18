import sys

arr = []

for _ in range(int(sys.stdin.readline())):
    inp = sys.stdin.readline()
    v = int(inp[0])
    if v == 1:
        arr.append(inp.split()[1])
    elif v == 2:
        if len(arr) == 0:
            print(-1)
            continue
        b = arr.pop()
        print(b)
    elif v == 3:
        print(len(arr))
    elif v == 4:
        if len(arr) == 0:
            print(1)
        else:
            print(0)
    elif v == 5:
        if len(arr) == 0:
            print(-1)
            continue
        print(arr[-1])