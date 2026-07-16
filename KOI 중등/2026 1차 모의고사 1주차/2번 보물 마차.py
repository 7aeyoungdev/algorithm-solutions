# https://jungol.co.kr/contest/4081/problem/2

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
t = [ list(map(int, input().split())) for _ in range(n) ]
s = list(map(int, input().split()))

t.sort()
s.sort()

ans = 0
pq = []
i = 0

for w in s:
    while i < n and t[i][0] <= w:
        heapq.heappush(pq, -t[i][1])
        i += 1
    
    if pq:
        ans -= heapq.heappop(pq)

print(ans)