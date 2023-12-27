n = int(input())
lst0 = []
lst1 = []
lst2 = []
lst3 = []
for i in range(n):
    n, a, b, c = input().split()
    a, b, c = int(a), int(b), int(c)
    lst0.append(n)
    lst1.append(a)
    lst2.append(b)
    lst3.append(c)

idx = lst1.index(max(lst1))
print(lst0[idx], list(reversed(sorted(lst2))).index(lst2[idx]) + 1, list(reversed(sorted(lst3))).index(lst3[idx]) + 1)