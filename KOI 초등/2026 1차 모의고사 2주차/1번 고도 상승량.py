# https://jungol.co.kr/contest/4083/problem/1

n = int(input())
a = list(map(int, input().split()))

ans = 0
s = a[0]

for i in range(1, n):
    if a[i] > a[i - 1]:
        ans = max(ans, a[i] - s)
    else:
        s = a[i]

print(ans)