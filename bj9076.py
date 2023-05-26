for i in range(int(input())):
    lst = sorted(list(map(int, input().split())))
    lst = lst[1:-1]
    if lst[-1] - lst[0] >= 4:
        print("KIN")
    else:
        print(sum(lst))