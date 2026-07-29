# https://jungol.co.kr/problem/12381

import heapq

n = int(input())
a = list(map(int, input().split()))

target = 1
pq = [] # 못 쓴 동전
ans = []

for coin in a:
    if coin > target:
        heapq.heappush(pq, coin)
    else:
        target += coin

        while pq and pq[0] <= target:
            target += heapq.heappop(pq)
        
    ans.append(target)

print(*ans, sep = '\n')