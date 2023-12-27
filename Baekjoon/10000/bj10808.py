s = list(input())
arr = [0 for i in range(26)]

for i in s:
    arr[ord(i) - ord('a')] += 1
for i in arr:
    print(i, end=" ")