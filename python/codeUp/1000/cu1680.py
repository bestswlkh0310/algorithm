# 20s + 2o == 100t + 11o
# 20s -9o == 100t

for t in range(1, 10):
    for s in range(1, 10):
        for o in range(10):
            if 20 * s - 9 * o == 100 * t:
                print(f"{s}{o}+{s}{o}={t}{o}{o}")