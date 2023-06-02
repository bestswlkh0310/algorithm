s = 1
for i in range(3, 10000, 2):
    s *= (i - 1) / i * (i + 1) / i
print(s * 4)