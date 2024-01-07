n = int(input())
lst = list(map(int, input().split()))
s = list(reversed(sorted(lst)))
for i in lst:
    print(i, s.index(i) + 1)