# https://jungol.co.kr/contest/4096/problem/1

a, b = map(int, input().split())
c, d = map(int, input().split())

e = [a, b, c, d]

spl = (b - a) + (d - c)
lap = max(e) - min(e)

print(min(spl, lap))