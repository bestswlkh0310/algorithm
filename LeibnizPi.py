s = 0
for k in range(10000000):
    s += (-1) ** k / (2 * k + 1)
print(s * 4)
