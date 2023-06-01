n, k = map(int, input().split())
lst = []
lst2 = []
for i in range(n):
    nam, s = input().split()
    lst.append(int(s))
    lst2.append(nam)
for i in range(n - 1):
    for j in range(n - 1):
        if lst[j] < lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
            lst2[j], lst2[j + 1] = lst2[j + 1], lst2[j]
for i in range(k):
    print(lst2[i])