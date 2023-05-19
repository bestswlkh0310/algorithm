n = int(input())
dic = dict()
for i in range(n):
    a, b = map(int, input().split())
    dic[a] = b

for (i, j) in sorted(dic.items()):
    print(i, j)