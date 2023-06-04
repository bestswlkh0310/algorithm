import sys

m = int(sys.stdin.readline())
arr = 0
xor = 0
for _ in range(m):
    inp = sys.stdin.readline()
    if int(inp[0]) <= 2:
        a, b = map(int, inp.split())
        if a == 1:
            arr += b
            xor ^= b
        else:
            arr -= b
            xor ^= b
    else:
        if inp.strip() == '3':
            sys.stdout.write(f"{arr}\n")
        else:
            sys.stdout.write(f"{xor}\n")
