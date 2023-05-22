# 일 더하기 일은요?
lst = input().split()
try:
    auth = lst[-1][-3:]
    lst[-1] = lst[-1][:-3]
    dic = {
        "일": 1,
        "이": 2,
        "삼": 3,
        "사": 4,
        "오": 5,
        "육": 6,
        "칠": 7,
        "팔": 8,
        "구": 9,
    }

    dic1 = {
        "십": 10 ** 1,
        "백": 10 ** 2,
        "천": 10 ** 3,
        "만": 10 ** 4,
        "십만": 10 ** 5,
        "백만": 10 ** 6,
        "천만": 10 ** 7,
        "억": 10 ** 8,
    }
# ex. 일천오백삼십오 더하기 오천일백오십팔만오천이백일십은요?

    def calc(a1, do, a2):
        s1 = 0
        s2 = 0
        if len(a1) > 1:
            for i in range(0, len(a1) - 1, 2):
                s1 += dic[a1[i]] * dic1[a1[i + 1]]
        if len(a2) > 1:
            for i in range(0, len(a2) - 1, 2):
                s2 += dic[a2[i]] * dic1[a2[i + 1]]
        if len(a1) % 2 == 1:
            s1 += dic[a1[-1]]
        if len(a2) % 2 == 1:
            s2 += dic[a2[-1]]
        if do == "더하기":
            return "귀요미 " * (s1 + s2)
        elif do == "빼기":
            return "곱빼기" * abs(s1 - s2)
        elif do == "나누기":
            return "갈! " * (s1 // s2)
        elif do == "곱하기":
            return "얍! " * (s1 * s2)


    def 인증(a):
        if a == "은요?" or a == "는요?":
            return True
        else:
            return False

    if 인증(auth):
        print(calc(lst[0], lst[1], lst[2]))
    else:
        print("갈!!!!!!!!!!!!!!!!!!!")
except Exception as e:
    print(e)
    # print("갈!!!!!!!!!!!!!!!!!!!")
