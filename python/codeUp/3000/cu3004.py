n = int(input())
lst = list(map(int, input().split()))
lst1 = lst.copy()
lst.sort()
dic = dict()
for (idx, k) in enumerate(lst):
    dic[k] = idx
for i in lst1:
    print(dic[i], end=" ")