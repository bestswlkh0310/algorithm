# 90i + 9j = 10k
for i in range(1, 10):
    for j in range(10):
        for k in range(1, 10):
            if 90 * i + 9 * j == 10 * k:
                print("%d%d%d-%d%d=%d%d" %(i, j, k, i, j, k, k))