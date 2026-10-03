# https://jungol.co.kr/contest/2499/problem/2

import sys
input = sys.stdin.readline

x = 10000
p = [0] * (x + 1)

for i in range(1, x + 1):
    p[i] = p[i - 1]

    s = str(i)
    if len(s) == len(set(s)):
        p[i] += 1

t = int(input())

ans = []

for i in range(t):
    n, m = map(int, input().split())
    ans.append(p[m] - p[n - 1])

print(*ans, sep = '\n')