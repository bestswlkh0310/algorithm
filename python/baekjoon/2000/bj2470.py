n = int(input())
lst = [*sorted([*map(int, input().split())])]

i = 0
j = n - 1
mn = abs(lst[i] + lst[j])
r1 = lst[i]
r2 = lst[j]

while i < j:
    v = abs(lst[i] + lst[j])
    # print(i, j)
    if v < mn:
        mn = v
        r1 = lst[i]
        r2 = lst[j]
    if abs(lst[i] + lst[j - 1]) < abs(lst[i + 1] + lst[j]):
        j -= 1
    elif abs(lst[i + 1] + lst[j]) < abs(lst[j - 1] + lst[i]):
        i += 1
    else:
        if lst[i] + lst[j - 1] < lst[i + 1] + lst[j]:
            j -= 1
        else:
            i += 1
print(r1, r2)

# 5
# -99 -98 0 1 96