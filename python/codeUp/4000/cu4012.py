n = input()
lst = list(map(int, input().split()))
for i in lst:
    print(i, list(reversed(sorted(lst))).index(i) + 1)