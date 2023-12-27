import sys
n, k = map(int, sys.stdin.readline().strip().split())
dic = dict()
dic1 = dict()
for i in range(n):
    inp = sys.stdin.readline().strip()
    dic[i + 1] = inp
    dic1[inp] = i + 1
for i in range(k):
    inp = sys.stdin.readline().strip()
    if inp.isdigit():
        sys.stdout.write(f"{dic[int(inp)]}\n")
    else:
        sys.stdout.write(f"{dic1[inp]}\n")