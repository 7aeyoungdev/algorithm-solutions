# https://jungol.co.kr/contest/4235/problem/4

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = -10**20

l = a[0] + 0 * k
for i in range(1, n):
    r = a[i] + i * k
    ans = max(ans, l - r)
    l = max(l, r)

l = a[0] - 0 * k
for i in range(1, n):
    r = a[i] - i * k
    ans = max(ans, r - l)
    l = min(l, r)

print(ans)