# 서로소인 두 자연수 a와 m의 값이 주어지면 a의 법 m에 대한 잉여역수 a*

# (a * b) == (1 + m) (mod m)
# 이때 b의 최소값
b = 1
a, m = map(int, input().split())

while True:
    if (b + m) % a == 0:
        b += m
        break
    b += m
print(b // a)
