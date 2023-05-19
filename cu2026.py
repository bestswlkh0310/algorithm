lst = list(input())
for (idx, k) in enumerate(lst):
    if ord(k) >= ord('A'):
        lst[idx] = ord(k) - ord('A') + 10
    else:
        lst[idx] = int(k)
for i in lst:
    s = i
    arr = [0] * 4
    for j in range(4):
        arr[j] = s % 2
        s //= 2
    for j in reversed(arr):
        print(j, end="")
    print(end=" ")