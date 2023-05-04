str = list(input())
sum = 0
cnt = 0
for i in range(1, len(str)):
    if str[i] != str[i - 1]:
        sum += 10
print(sum)