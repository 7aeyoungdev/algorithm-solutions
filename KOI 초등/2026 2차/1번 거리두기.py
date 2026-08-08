# https://jungol.co.kr/problem/21025

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = [0] * n

b[-1] = a[-1]

for i in range(-2, -n - 1, -1):
    b[i] = min(a[i], b[i + 1] - k)

print(*b)