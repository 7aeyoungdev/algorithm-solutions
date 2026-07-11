# https://usaco.org/index.php?page=viewproblem2&cpid=1301

n, k = map(int, input().split())
d = list(map(int, input().split()))

ans = 1 + k

for i in range(1, n):
    day = d[i] - d[i - 1]
    ans += min(1 + k, day)

print(ans)