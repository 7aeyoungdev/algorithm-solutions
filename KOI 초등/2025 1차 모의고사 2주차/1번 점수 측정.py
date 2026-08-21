# https://jungol.co.kr/contest/2490/problem/1

n, m = map(int, input().split())
k = [ int(input()) for _ in range(m) ]
a = 3 * (n - m)
print((sum(k) - a) / n, (sum(k) + a) / n)