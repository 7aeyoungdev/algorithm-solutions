# https://jungol.co.kr/contest/2483/problem/1

n, a, b = map(int, input().split())

x, y = 1, 1

def day(p, q):
    p += a
    q += b

    if p < q:
        p, q = q, p
    elif p == q:
        q -= 1

    return p, q

for i in range(n):
    x, y = day(x, y)

print(x, y)