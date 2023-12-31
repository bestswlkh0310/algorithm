import sys
input=sys.stdin.readline
print=sys.stdout.write
for _ in range(int(input())):
    n, k = map(int, input().split())
    lst = [*sorted(map(int, input().split()))]
    l = 0
    r = n - 1
    s = None
    t = False
    cnt = 0
    re = []
    e = True
    while l < r:
        s = lst[l] + lst[r]
        re.append(s)
        if lst[l] + lst[r] > k:
            r -= 1
        elif lst[l] + lst[r] < k:
            l += 1
        else:
            e = False
            l += 1
    # print('s -',s, re)
    if e:
        print(f'{re.count(s) + re.count(s-(k-s))}\n')
    else: # 1 3 5 7 9
        print(f'{re.count(k)}\n')