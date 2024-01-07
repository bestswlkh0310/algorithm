# 2754 -학점계산
s = 0
inp = list(input())
a = inp[0]
if a == 'F':
    print("0.0")
    exit(0)
b = inp[1]
if a == 'A': s += 4
elif a == 'B': s += 3
elif a == 'C': s += 2
elif a == 'D': s += 1

if b == '+': s += 0.3
elif b == '-': s -= 0.3
print(float(s))