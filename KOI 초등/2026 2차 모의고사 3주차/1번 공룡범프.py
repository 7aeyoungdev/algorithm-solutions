# https://jungol.co.kr/contest/4242/problem/1

n, c, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
std = 0
w = 0

for i in range(n):
    if a[i] > k:
        ans = -1
        break

    if std < c and w + a[i] <= k:
        std += 1
        w += a[i]
    else:
        ans += 1
        std = 1
        w = a[i]

print(ans)