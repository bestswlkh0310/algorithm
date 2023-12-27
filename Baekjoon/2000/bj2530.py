# 2530 - 인공지능 시계
a, b, c = map(int, input().split())
d = int(input())

sum = (a * 60 * 60 + b * 60 + c + d + 60 * 60 * 24) % (60 * 60 * 24)
print(sum // (60 * 60), sum % (60 * 60) // 60, sum % 60)