arr = []

for _ in range(int(input())):
    n = input()
    if n == '+':
        arr.append(arr[-1] + 1)
    elif n == '-':
        arr.append(arr[-1] - 1)
    elif n == '0':
        del arr[-1]
    else:
        arr.append(int(n))
print(sum(arr))