import random

print("***** 1~100 사이 숫자 맞히기 게임 *****")
answer = random.randint(1, 100)
s = 0
def what_num():
    global s
    s += 1
    n = int(input("숫자를 입력하세요 > "))
    if answer > n:
        print("%d 보다는 큰 수 입니다. 무엇 일까요?" %n)
    elif answer < n:
        print("%d 보다는 작은 수 입니다. 무엇 일까요?" %n)
    else:
        print("정답!!! 정답은 %d 입니다. %d 번 만에 맞췄네요!" %(n, s))
        return 0
    return 1
while what_num():
    pass