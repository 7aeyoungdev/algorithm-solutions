# https://jungol.co.kr/problem/12371

n, m = map(int, input().split())
a = [ list(map(int, input().split())) for _ in range(n) ]
best = [0] * n
for i in range(n):
    best[i] = max(a[i])

ans = [0] * m
for k in range(m):
    cnt = 0
    for i in range(n):
        if a[i][k] < best[i]:
            cnt += 1
    ans[k] = cnt

print(*ans)