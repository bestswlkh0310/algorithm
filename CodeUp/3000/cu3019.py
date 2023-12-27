import operator
lst1 = []
lst2 = []
for i in range(int(input())):
    a, b, c, d = input().split()
    b, c, d = int(b), int(c), int(d)
    lst1.append(a)
    lst2.append(b*10000+c*100+d)
for i in sorted(lst2):
    print(lst1[lst2.index(i)])
