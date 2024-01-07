def nSum(str):
    s = 0
    for i in str:
        if i.isdigit():
            s += int(i)
    return s

def compare(a, b):
    if len(a) < len(b):
        return True
    elif len(a) > len(b):
        return False
    else:
        s1 = nSum(a)
        s2 = nSum(b)
        if s1 != s2:
            return s1 < s2
        else:
            return a < b

n = int(input())
lst = [input() for _ in range(n)]

for i in range(n):
    for j in range(n - i - 1):
        if compare(lst[j + 1], lst[j]):
            lst[j], lst[j + 1] = lst[j + 1], lst[j]
for i in lst:
    print(i)
