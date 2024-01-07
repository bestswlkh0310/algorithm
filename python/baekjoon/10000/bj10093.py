a, b = map(int, input().split())
mx = max(a, b)
mn = min(a, b)
s = mx - mn - 1
if s == -1:
    s = 0
print(s)
for i in range(mn + 1, mx):
    print(i, end=" ")