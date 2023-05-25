lst = sorted(list(map(int, input().split())))
s = list(input())
for i in s:
    if i == "A":
        print(min(lst), end=" ")
    elif i == "B":
        print(sum(lst) - max(lst) - min(lst), end=" ")
    else:
        print(max(lst), end=" ")