s = 0
mx = 0
for i in range(4):
    a, b = map(int, input().split())
    s += -a + b
    mx = s if mx < s else mx
print(mx)