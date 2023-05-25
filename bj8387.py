n = int(input())
str1 = list(input())
str2 = list(input())
cnt = 0
for i in range(n):
    if str1[i] == str2[i]:
        cnt += 1
print(cnt)