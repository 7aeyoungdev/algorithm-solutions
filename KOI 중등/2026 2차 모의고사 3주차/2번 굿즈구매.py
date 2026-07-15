# https://jungol.co.kr/contest/4243/problem/2

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

first = []
min_set = 10**20

for i in range(n):
    x, y = map(int, input().split())
    first.append(x)
    min_set = min(min_set, x + y)

first.sort()

ans = 2 * (m // min_set)

cost = 0
for i in range(n):
    cost += first[i]
    if cost > m:
        break

    charge = m - cost
    ans = max(ans, i + 1 + 2 * (charge // min_set))

print(ans)