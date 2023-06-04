n = int(input())
lst = list(map(int, input().split()))

for _ in range(int(input())):
    m, k = map(int, input().split())
    if m == 1:
        for (idx, j) in enumerate(lst):
            if (idx + 1) % k == 0:
                lst[idx] = 1 if j == 0 else 0
    else:
        i = k - 1
        w = 0
        while 0 <= i - w and i + w < n:
            if lst[i + w] != lst[i - w]:
                break
            else:
                if w == 0:
                    lst[i] = 1 if lst[i] == 0 else 0
                else:
                    lst[i + w] = 1 if lst[i + w] == 0 else 0
                    lst[i - w] = 1 if lst[i - w] == 0 else 0
            w += 1
for (idx, i) in enumerate(lst):
    print(end=f"{i} ")
    if (idx + 1) % 20 == 0:
        print()