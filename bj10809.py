lst = list(input())
arr = [-1] * 26
# abcd
for (idx, k) in enumerate(lst):
    if arr[ord(k) - ord('a')] == -1:
        arr[ord(k) - ord('a')] = idx
for i in arr:
    print(i, end=" ")