n = int(input())
arr = [[None, None] for _ in range(n)]

for i in range(n):
    s, l, r = input().split()
    if l == '.':
        l = None
    else:
        l = ord(l) - ord('A')
    if r == '.':
        r = None
    else:
        r = ord(r) - ord('A')
    arr[ord(s) - ord('A')] = [l, r]

r1 = ""
r2 = ""
r3 = ""

def exp(v, i):
    global r1, r2, r3
    r1 += chr(i + ord('A'))
    if v[0] != None:
        exp(arr[v[0]], v[0])
    r2 += chr(i + ord('A'))
    if v[1] != None:
        exp(arr[v[1]], v[1])
    r3 += chr(i + ord('A'))
    
exp(arr[0], 0)
print(r1)
print(r2)
print(r3)
