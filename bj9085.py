for i in range(int(input())):
    n = int(input())
    lst = list(map(int, input().split()))
    sum = 0
    for j in range(n):
        sum += lst[j]
    print(sum)