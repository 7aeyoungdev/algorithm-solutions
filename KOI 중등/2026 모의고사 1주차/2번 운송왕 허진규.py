# https://jungol.co.kr/contest/4230/problem/2

import sys
input = sys.stdin.readline

n, m, c = map(int, input().split())
t = list(map(int, input().split()))
t.sort()

def check(limit_time):
    bus = 1
    std = 1
    start_time = t[0]

    for i in range(1, n):
        wait_time = t[i] - start_time

        if std < c and wait_time <= limit_time:
            std += 1
        else:
            bus += 1
            std = 1
            start_time = t[i]

    return bus <= m

l, r = 0, t[-1] - t[0]
ans = r

while l <= r:
    mid = (l + r) // 2 # mid : 최대 대기 시간 
    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)