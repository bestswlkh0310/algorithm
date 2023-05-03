h2, m2, s2 = map(int, input().split(':'))
h1, m1, s1 = map(int, input().split(':'))

sum = ((h1 - h2) * 3600 + (m1 - m2) * 60 + s1 - s2 + 60 * 60 * 24) % (60 * 60 * 24)
h = sum // 3600
m = (sum - sum // 3600 * 3600) // 60
s = sum % 60

print("%02d:%02d:%02d" %(h, m, s))