for _ in range(int(input())):
    n, l = map(int, input().split())
    arr = [False] * l
    cnt = 0
    for i in range(n):
        k = int(input())
        if not arr[k - 1]:
            arr[k - 1] = True
        else:
            cnt += 1
    print(cnt)