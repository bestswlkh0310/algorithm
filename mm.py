# 현아 공주님은 비둘기를 매우 싫어하세요.
# 현아 공주님은 특수한 능력을 갖고 있지요.
# 비둘기는 n일마다 오지요.
# 현아 공주님은 m일마다 비둘기를 퇴치할 수 있다.
# 비둘기를 퇴치하지 못 한 날은 스트레스 지수가 c만큼 올라간다.
# 비둘기를 퇴치한 날에는 스트레스 지수가 k만큼 줄어든다.
# 5월의 어느 d1일 부터 d2일 까지 비둘기와의 전투가 끝난 후 스트레스 지수를 출력하는 프로그램을 만드시오.
# 스트레스 지수가 0 미만이면 "기부니가 좋쿤요~"를 출력하세요.
# while, for 문 사용금지!!
# for문은 테스트케이스 돌릴 때만 사용 허용

def kill(i, end):
    global cnt, n, m, c, k

    if i % n == 0 and i % m == 0:
        cnt -= k
    elif i % n == 0:
        cnt += c

    if i == end:
        return
    return kill(i + 1, end)

cnt = 0
t, n, k, d1, d2 = map(int, input().split())
arr = []
for i in range(t):
    m, c = map(int, input().split())
    kill(1, d2 - d1 + 1)
    arr.append(cnt)
    cnt = 0
    s = 0
mn = min(arr)
if mn < 0:
    print("기부니가 좋쿤요~")
else:
    print(mn)


# 3 5 2 1 20
# 3 5
# 5 7
# 2 10

# answer: 기부니가 좋쿤요~


# 3 1 10 1 31
# 5 7
# 5 3
# 10 5

# answer: 15