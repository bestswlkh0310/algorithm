for i in range(int(input())):
    lst = [i for i in list(map(int, input().split())) if i % 2 == 0]
    print(sum(lst), min(lst))