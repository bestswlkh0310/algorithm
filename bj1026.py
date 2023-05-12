n = int(input())
lst1 = list(map(int, input().split()))
lst2 = list(map(int, input().split()))

lst1.sort()
lst2.sort(reverse=True)

s = 0
for i in range(n):
    s += lst1[i] * lst2[i]
print(s)