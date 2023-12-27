lst = list(input())
a = []
for i in range(1, len(lst) - 1):
    for j in range(i + 1, len(lst)):
        s1 = lst[:i]
        s2 = lst[i:j]
        s3 = lst[j:]
        s1.reverse()
        s2.reverse()
        s3.reverse()
        a.append("".join(s1 + s2 + s3))

a.sort()
print(a[0])
