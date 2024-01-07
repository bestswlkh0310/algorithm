a, b = map(int, input().split())
lst = list(map(int, input().split()))
s = [0 for _ in range(a + 1)]

for i in range(a):
    s[i + 1] = s[i] + lst[i]
for _ in range(b):
    z, x = map(int, input().split())
    print(s[x] - s[z - 1])