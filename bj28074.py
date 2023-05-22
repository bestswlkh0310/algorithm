l = {
    'M':False,
     'O':False,
     'B':False,
     'I':False,
     'S':False
}

ls = ['M', 'O', 'B', 'I', 'S']

lst = list(input())
t = True
for i in lst:
    if i in ls:
        l[i] = True
for i in l.values():
    if not i: t = False

if t:
    print("YES")
else:
    print("NO")