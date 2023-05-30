import random
import time
print("********주사위 프로그램********")
print("3초 후 주사위 결과를 알려드립니다.")
n = random.randint(1, 6)
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print("결과는!!! :", n)