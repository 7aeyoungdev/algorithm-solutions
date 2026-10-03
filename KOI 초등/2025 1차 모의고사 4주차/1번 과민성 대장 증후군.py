# https://jungol.co.kr/contest/2499/problem/1

n, m = map(int, input().split())
a = list(map(int, input().split()))
s = 0

ans = 0

for i in a:
    s += i
    if s < 0:
        s = 0
    if s >= m:
        ans += 1

print(ans)