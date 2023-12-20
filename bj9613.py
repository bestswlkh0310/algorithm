import math
for _ in range(int(input())):
    s = 0
    lst = list(map(int, input().split()))
    k = lst[0]
    del lst[0]
    for i in range(k):
        for j in range(i + 1, k):
            a = lst[i]
            b = lst[j]
            s += math.gcd(a, b)
    print(s)