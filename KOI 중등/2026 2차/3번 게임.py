# https://jungol.co.kr/problem/21028

import sys
import heapq

input = sys.stdin.readline

n, m, q = map(int, input().split())
e = [0] + list(map(int, input().split()))

g = [ [] for _ in range(n + 1) ]
for i in range(m):
    a, b, c = map(int, input().split())
    g[a].append( (b, c) )
    g[b].append( (a, c) )

limit = [0] * (n + 1) # 이길 수 있는 k 의 최댓값
count = [0] * (n + 1) # 이기는 방으로 가는 통로 개수
visit = [False] * (n + 1)

pq = []
for i in range(1, n + 1):
    if e[i] == 1:
        heapq.heappush(pq, (-10**20, i) ) # 출구가 있는 방

limit_min = 10**20

while pq:
    p, x = heapq.heappop(pq)
    p = -p

    if visit[x]:
        continue
    visit[x] = True

    limit[x] = min(limit_min, p) 
    limit_min = limit[x]

    for nx, c in g[x]:
        if not visit[nx]:
            count[nx] += c
            heapq.heappush(pq, (-count[nx], nx) )

ans = []
for i in range(q):
    s, k = map(int, input().split())
    if limit[s] >= k:
        ans.append('YES')
    else:
        ans.append('NO')

print(*ans, sep = '\n')