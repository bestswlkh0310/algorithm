lst = []
a = [0] * (1001)
for i in range(10):
    b = int(input())
    lst.append(b)
    a[b] += 1
print(sum(lst) // 10)
print(a.index(max(a)))