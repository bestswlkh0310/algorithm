n = int(input())

a1 = []
a2 = []

for _ in range(n):
    a, b = map(int, input().split())
    a1.append(a)
    a2.append(b)

a1.append(a1[0])
a2.append(a2[0])

s = 0

for i in range(n):
    s += a1[i] * a2[i + 1] - a1[i + 1] * a2[i]

print(abs(s / 2))