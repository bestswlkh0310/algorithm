a, b = map(int, input().split())
lst = sorted(input().split())
mo = ('a', 'e', 'i', 'o', 'u')
def A(i, s):
    if i == a:
        cnt = 0
        cnt1 = 0
        for k in s:
            if k in mo:
                cnt += 1
            else:
                cnt1 += 1
        if cnt != 0 and cnt1 > 1:
            print(s)
        return
    for j in range(i, b):
        com = s + lst[j]
        if lst[j] not in s and com == "".join(sorted(list(com))):
            A(i + 1, s + lst[j])
for i in lst:
    A(1, i)