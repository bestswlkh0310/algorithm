n = int(input())
lst = list(map(int, input().split()))
lst1 = sorted(lst)
lst2 = lst1.copy()
lst2.reverse()
if lst1 == lst2:
    print("섞임")
elif lst1 == lst:
    print("오름차순")
elif lst2 == lst:
    print("내림차순")
else:
    print("섞임")