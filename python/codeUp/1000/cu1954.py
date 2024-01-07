n = int(input())

def A(i):
    if i == 0:
        return
    print("*"*i)
    A(i - 1)
A(n)