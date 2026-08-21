# https://jungol.co.kr/contest/2483/problem/3

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
c = list(map(int, input().split()))
t = list(map(int, input().split()))

limit = [ c[i] - t[i] for i in range(n) ]
limit.sort(reverse = True)

ans = []

for i in range(q):
    v, s = map(int, input().split())

    if s < limit[v - 1]:
        ans.append("YES")
    else:
        ans.append("NO")

print(*ans, sep = '\n')