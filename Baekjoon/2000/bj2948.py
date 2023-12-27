d, m = map(int, input().split())
s = 0
ar = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0, m - 1):
    s += ar[i]
s += d
di = {
    1 : "Thursday",
    2 : "Friday",
    3 : "Saturday",
    4 : "Sunday",
    5 : "Monday",
    6 : "Tuesday",
    0 : "Wednesday"
}
print(di[s % 7])