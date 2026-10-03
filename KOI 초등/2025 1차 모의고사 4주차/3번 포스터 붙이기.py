# https://jungol.co.kr/contest/2499/problem/3

import sys

input = sys.stdin.readline

n = int(input())

h = []
ans = 0

for i in range(n):
    d, w = map(int, input().split())

    while h and h[-1] > w:
        h.pop()

    if not h or h[-1] < w:
        h.append(w)
        ans += 1

print(ans)