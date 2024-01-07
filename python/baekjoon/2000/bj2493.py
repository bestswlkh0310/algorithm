n = int(input())
lst = [*map(int, input().split())]

stack = []
v = None
for (idx, i) in enumerate(lst):
    while len(stack) > 0 and stack[-1][1] < i:
        v = stack.pop()
    if len(stack) > 0:
        print(stack[-1][0] + 1)
    else:
        print(0)
    stack.append((idx, i))
