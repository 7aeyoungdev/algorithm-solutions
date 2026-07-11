# https://usaco.org/index.php?page=viewproblem2&cpid=785

import sys

sys.stdin = open('outofplace.in', 'r')
sys.stdout = open('outofplace.out', 'w')

n = int(input())
c = [ int(input()) for _ in range(n) ]

s = c.copy()
s.sort()

ans = 0

for i in range(n):
    if c[i] != s[i]:
        ans += 1

print(max(0, ans - 1))