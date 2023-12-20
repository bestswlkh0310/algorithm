arr = []

try:
    while True:
        inp = input()
        if inp == ' ':
            break
        arr.append(inp)
except:
    pass

arr1 = [i for i in arr if i[0] != '0']

arr1 = sorted(arr1, key=lambda x: int(x) * 10 ** (9 - len(x) - 0.0001 * len(x)))

arr2 = [i for i in arr if i[0] == '0']

arr2 = sorted(arr2, key=lambda x: int('1' + (x)) * 10 ** (9 - len(x) - 0.0001 * len(x)))

arr1.reverse()

arr2.reverse()

arr3 = arr1 + arr2

# print(arr3)

for i in range(len(arr3) - 1):
    for j in range(len(arr3) - 1 - i):
        if int(str(arr3[j]) + str(arr3[j + 1])) < int(str(arr3[j + 1]) + str(arr3[j])):
            # print('splited', arr3[j], arr3[j + 1])
            arr3[j], arr3[j + 1] = arr3[j + 1], arr3[j]

for i in arr3:
    print(end=f"{i}")

print()

# 92
# 91
# 9
# 78
# 7
# 888
# 76