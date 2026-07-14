# https://jungol.co.kr/contest/4236/problem/4

import sys
import bisect
input = sys.stdin.readline

n, k = map(int, input().split())
g = [ list(map(int, input().split())) for _ in range(n) ]
g.sort(key = lambda x: (x[1], x[0]))

def check(win):
    end_time = [-1] * (k - 1)
    time = -1
    cnt = 0
    for s, e in g:
        if s <= time:
            continue

        i = bisect.bisect_right(end_time, s - 1)

        if i > 0:
            end_time[i - 1] = e
            end_time.sort()
        else:
            time = e
            cnt += 1
            if cnt > win:
                return False
    
    return True

l, r = 0, n
ans = n

while l <= r:
    mid = (l + r) // 2

    if check(mid):
        ans = mid
        r = mid - 1
    else:
        l = mid + 1

print(ans)