s = input()
l = len(s)
s = int(s)
r = int('1'*l)
while l <= 1_000_000:
    import sys
    if not (((r % s) + s) % s):
        print(l)
        exit(0)
    r = r * 10 + 1
    l += 1
print(-1)
