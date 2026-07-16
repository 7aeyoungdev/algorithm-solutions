# https://jungol.co.kr/contest/4081/problem/3

import heapq

n, m = map(int, input().split())
w = list(map(int, input().split()))

n -= 1

l = min(w)
d = [10**20] * l # l 로 나누었을 때 해당 나머지를 가지는 최소 무게
d[0] = 0

pq = [(0, 0)] # 무게 합, 나머지

while pq:
    s, r = heapq.heappop(pq)
    if s > d[r]:
        continue

    for x in w:
        ns = s + x
        nr = ns % l

        if ns < d[nr]:
            d[nr] = ns
            heapq.heappush(pq, (ns, nr))

ans = 0

for i in range(l):
    if d[i] <= n:
        ans += (n - d[i]) // l + 1

print(ans - 1)