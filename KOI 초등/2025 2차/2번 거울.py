# https://jungol.co.kr/problem/8605

n, s = map(int, input().split())
a = list(map(int, input().split()))

l, r = 0, n - 1

while l <= r:
    if n % 2 == 0:
        s = 2 * a[l] - s
        l += 1
    else:
        s = 2 * a[r] - s
        r -= 1

    n -= 1

print(s)