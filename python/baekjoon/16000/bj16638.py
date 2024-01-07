n = int(input())
lst = list(input())


def calc(a, b, c):
    a, b = int(a), int(b)
    if c == "*": return a * b
    if c == "+": return a + b
    if c == "-": return a - b

def calc2(s):
    l = len(s)
    for i in range(2, l, 2):
        m = s[i - 1]
        if m == "+":
            s[i] = int(s[i]) + int(s[i - 2])
        if m == "-":
            s[i] = int(s[i - 2]) - int(s[i])
    return s[-1]

def calc1(s):
    t = True
    while t:
        f = True
        for i in range(1, len(s), 2):
            if s[i] == '*':
                s[i] = int(s[i - 1]) * int(s[i + 1])
                s[i - 1] = s[i + 1] = "None"
                s = [i for i in s if i != "None"]
                f = False
                break
        if f:
            t = False
    return calc2(s)


if n == 1:
    print(lst[0])
    exit(0)
elif n == 3:
    print(calc1(lst))
    exit(0)


mx = -999999999999999999
def A(start, s):
    global n, mx
    lst1 = lst[:]
    for k in s:
        idx = k * 2 + 1
        lst1[idx] = str(calc(lst1[idx - 1], lst1[idx + 1], lst1[idx]))
        lst1[idx - 1] = "None"
        lst1[idx + 1] = "None"
    lst1 = [i for i in lst1 if i != "None"]
    result = calc1(lst1)
    mx = mx if mx > result else result
    for j in range(start + 2, n // 2):
        ar = s[:]
        ar.append(j)
        A(j, ar)
for i in range(n // 2):
    A(i, [i])

print(mx)