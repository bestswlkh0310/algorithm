k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]
# sort priority: length, value
lst = [*sorted(lst, key=lambda x: (len(str(x)), x), reverse=True)]

best = sorted(lst, key=lambda x: -len(str(x)))[0]
for j in range(k - 1):
    for i in range(k - 1 - j):
        if int(str(lst[i]) + str(lst[i + 1])) < int(str(lst[i + 1]) + str(lst[i])):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

# print
t = False
for i in lst:
    if i == best and not t:
        t = True
        print(str(i) * (n - k + 1), end='')
    else:
        print(i, end='')