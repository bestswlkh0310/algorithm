k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]
lst = [*sorted(lst, key=lambda x: (x + 1) * 10 ** (k - len(str(x))) - 1 - len(str(x)) * 0.01, reverse=True)]
newLst = sorted(lst, key=lambda x: 12 - len(str(x)))
bst = newLst[0]
for j in range(len(lst) - 1):
    for i in range(len(lst) - 1 - j):
        if int(str(lst[i]) + str(lst[i + 1])) < int(str(lst[i + 1]) + str(lst[i])):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
t = False
for i in lst:
    if i == bst and not t:
        print(str(i) * (n - k), end='')
        t = True
    print(i, end='')
