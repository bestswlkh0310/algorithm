import math


def normalized(x, y):
    return x / ((x ** 2 + y ** 2) ** 0.5), y / ((x ** 2 + y ** 2) ** 0.5)

for i in range(180):
    print(normalized(1, math.tan(math.radians(i))))
    if i == 90:
        print()