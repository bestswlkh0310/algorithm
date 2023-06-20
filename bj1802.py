def check(lst):
    l = len(lst)
    mid = l // 2
    if l == 1:
        return True
    t = False
    for i in range(mid):
        if lst[i] == lst[l - i - 1]:
            t = True
    if t:
        return False
    if lst[mid - 1] == lst[mid]:
        return check(lst[:mid])
    else:
        return check(lst[mid + 1:])

for _ in range(int(input())):
    n = list(input())
    print("YES" if check(n) else "NO")
