sum = 0
n = int(input())
for i in range(n):
    inp = int(input())
    if 10000 <= inp <= 40000:
        sum += inp
print('가격의 평균:', sum // n)
