# https://jungol.co.kr/contest/4081/problem/1

n = int(input())
p = list(map(int, input().split()))

ans = 0

for i in range(1, n):
    if p[n - i] < p[n - i - 1]:
        ans = n - i
        break

print(ans)