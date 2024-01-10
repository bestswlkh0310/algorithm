n = int(input())
n1 = str(n)
chkLst = [*map(int, list(n1))]

def check(x: int) -> bool:
    for c in chkLst:
        if x % c:
            return False
    return True

while True:
    check(n1)