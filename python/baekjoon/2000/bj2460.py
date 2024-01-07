s = 0
mx = 0
for i in range(10):
    a, b = map(int, input().split())
    s += -a + b
    if mx < s:
        mx = s
print(mx)