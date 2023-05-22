n = int(input())
lst = list(map(int, input().split()))
s1 = 0
s2 = 0
for i in lst:
    s1 += (i // 30 + 1) * 10
for i in lst:
    s2 += (i // 60 + 1) * 15
if s1 == s2: print("Y M", end=" ")
elif s1 < s2: print("Y", end=" ")
else: print("M", end=" ")
print(min(s1, s2))