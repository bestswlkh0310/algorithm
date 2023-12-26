n = int(input())
lst1 = [i for i in list(map(int, input().split()))]

lst2 = sorted(lst1)

for i in lst1:
    v = lst2.index(i)
    print(v)
    lst2[v] = None