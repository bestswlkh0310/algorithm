inp = int(input())
for i in range(inp):
    k = int(input())  # 층
    n = int(input())  # 호
    arr = [i + 1 for i in range(n)]
    for j in range(1, k + 1):  # 층
        arrr = [0 for i in range(n)]
        for r in range(n):  # 각 층 별 객체
            sum = 0
            for k in range(r + 1):
                sum += arr[k]
            arrr[r] = sum
        arr = arrr
    print(arr[-1])