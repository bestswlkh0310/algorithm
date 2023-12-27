import math
for i in range(int(input())):
    print([i for i in list(str(math.factorial(int(input())))) if i != '0'][-1])
