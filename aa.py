
i = int(input())
j = int(input())

n = (4 * i - j) / 2
if n % 1 != 0.0:
    print("오류")
else:
    print(int(i - n), int(n))