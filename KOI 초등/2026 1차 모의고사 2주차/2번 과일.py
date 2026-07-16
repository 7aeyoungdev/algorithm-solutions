# https://jungol.co.kr/contest/4083/problem/2

import bisect

n, m ,k = map(int, input().split())
s = list(map(int, input().split()))
s.append(0)
s.sort()

ans = 0

for x in s:
    if abs(x) * 2 <= k:
        turn = k - abs(x) * 2

        if x <= 0:
            cnt = bisect.bisect_right(s, turn)- bisect.bisect_left(s, x)
            ans = max(ans, cnt)

        if x >= 0:
            cnt = bisect.bisect_right(s, x) - bisect.bisect_left(s, -turn)
            ans = max(ans, cnt)

print(ans - 1)