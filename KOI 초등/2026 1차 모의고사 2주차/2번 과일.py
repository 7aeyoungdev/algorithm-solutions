# https://jungol.co.kr/contest/4083/problem/2

import bisect

n, m ,k = map(int, input().split())
s = list(map(int, input().split()))
s.append(0)
s.sort()

ans = 0

for i in range(n + 1):
    # left
    if s[i] <= 0 and -s[i] * 2 <= k:
        right = k - (-s[i] * 2)
        j = bisect.bisect_right(s, right)
        ans = max(ans, j - i)
    
    # right
    if s[i] >= 0 and s[i] * 2 <= k:
        left = k - s[i] * 2
        j = bisect.bisect_left(s, -left)
        ans = max(ans, i - j + 1)

print(ans - 1)