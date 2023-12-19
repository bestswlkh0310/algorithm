import functools

k, n = map(int, input().split())

lst = []

for _ in range(k):
    n1 = int(input())
    lst.append(n1)

lst = list(reversed(sorted(lst, key=lambda x: (x + 1) * 10 ** (k - len(str(x))) - 1 - len(str(x)) * 0.01)))

newLst = sorted(lst, key=lambda x: 12 - len(str(x)))

bst = newLst[0]

for i in range(len(lst) - 1):
    if int(str(lst[i]) + str(lst[i + 1])) < int(str(lst[i + 1]) + str(lst[i])):
        # print('splited', lst[i], lst[i + 1])
        lst[i], lst[i + 1] = lst[i + 1], lst[i]
# print(lst)
t = False

for i in lst:
    if i == bst and not t:
        print(str(i) * (n - k), end='')
        t = True
    print(i, end='')