# https://jungol.co.kr/contest/2490/problem/2

n = int(input())
a, pa, b, pb = map(int, input().split())

best = 0

lemon_all = n // pa

for lemon in range(lemon_all + 1):
    money = n - pa * lemon
    sugar = money // pb
    taste = a * lemon + b * sugar

    if taste > best:
        best = taste
        ans = (lemon, sugar)

print(*ans)