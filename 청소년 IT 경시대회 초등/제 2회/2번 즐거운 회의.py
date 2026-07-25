# https://jungol.co.kr/problem/12352

import sys
input = sys.stdin.readline

n, m, t = map(int, input().split())

times = [ list(map(int, input().split())) for _ in range(n) ]

diff = [0] * (t + 1)
for i in range(m):
    c, d = map(int, input().split())

    s = max(times[c - 1][0], times[d - 1][0])
    e = min(times[c - 1][1], times[d - 1][1])

    if s < e:
        diff[s] += 1
        diff[e] -= 1

cnt = 0

for i in range(t):
    cnt += diff[i]
    print(cnt)