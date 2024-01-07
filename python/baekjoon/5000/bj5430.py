import sys

input = sys.stdin.readline

for _ in range(int(input())):
    p = list(input())
    n = int(input())
    inp = input().strip()
    lst = [] if len(inp) == 2 else inp[1:-1].split(',')
    t = 0
    k = True
    for i in p:
        if i == 'D':
            if len(lst) == 0:
                print('error')
                k = False
                break
            del lst[t]
        elif i == 'R':
            t = 0 if t == -1 else -1
    if not k: continue

    print(str([*map(int, (lst[::-1] if t == -1 else lst))]).replace(' ', ''))