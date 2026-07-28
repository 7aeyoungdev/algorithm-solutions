# https://jungol.co.kr/problem/12365

n = int(input())
a = list(map(int, input().split()))

dl = [0] * n
dl[0] = a[0]
for i in range(1, n):
    dl[i] = max(a[i], dl[i - 1] + a[i])

dr = [0] * n
dr[-1] = a[-1]
for i in range(n - 2, -1, -1):
    dr[i] = max(a[i], dr[i + 1] + a[i])

ans = [0] * n
for i in range(n):
    ans[i] = dl[i] + dr[i] - a[i]

print(*ans)