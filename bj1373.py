lst = list(map(int, list(input())))
lst.reverse()
arr = []
for i in range(0, len(lst) - 2, 3):
    s = lst[i] + lst[i + 1] * 2 + lst[i + 2] * 4
    arr.append(s)
ss = 0
lst = lst[len(lst) // 3 * 3:]
for (idx, i) in enumerate(lst):
    ss += i * 2 ** idx
if ss != 0:
    print(end=f"{ss}")
for i in arr:
    print(end=f"{i}")