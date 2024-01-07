n = int(input())
sum = 0

for i in range(n): sum += i + 1

for i in range(n):
    for j in range(i + 1):
        print(sum,end=" ")
        sum -= 1
    print()