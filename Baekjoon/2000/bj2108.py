import sys
n = int(sys.stdin.readline())
s = []
arr = [0 for i in range(8001)]
for i in range(n):
    inp = int(sys.stdin.readline())
    arr[inp + 4000] += 1
    s.append(inp)
s.sort()
result = sum(s) / n
print(round(result))
print(s[len(s)//2])
mx = max(arr)
if arr.count(mx) >= 2:
    arr[arr.index(mx)] = -1
print(arr.index(mx)-4000)
print(s[-1] - s[0])