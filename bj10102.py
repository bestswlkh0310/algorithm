# 10102 - 개표
n = int(input())
s = input()
a = s.count('A')
b = s.count('B')
if a > b: print("A")
elif a == b: print("Tie")
else: print("B")