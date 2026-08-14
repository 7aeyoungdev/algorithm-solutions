# https://jungol.co.kr/problem/8566

import heapq

n, p = map(int, input().split())
a = list(map(int, input().split()))

pq = []
s = 0

ans = []

for i in range(n):
    heapq.heappush(pq, a[i])
    s += a[i]

    while pq and s - pq[0] >= p:
        s -= heapq.heappop(pq)

    if s < p:
        ans.append(-1)
    else:
        ans.append(len(pq))

print(*ans)