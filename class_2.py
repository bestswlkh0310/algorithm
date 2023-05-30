import random
import datetime
import time
print("***********오늘의 로또 추첨***********")
y, m, d = str(datetime.datetime.now()).split()[0].split('-')
print(f"{y} 년 {m} 월 {d} 일")
print("3초 후 오늘의 로또 번호를 알려드립니다.")
for i in range(3, 0, -1):
    print(i)
    time.sleep(1)
print("결과는 !!!")
for i in range(7):
    print(random.randint(1, 45))