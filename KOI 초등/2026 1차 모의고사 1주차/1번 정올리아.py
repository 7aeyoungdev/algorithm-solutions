# https://jungol.co.kr/contest/4080/problem/1

import sys
input = sys.stdin.readline

n = int(input())
ans = [0] * 4

for i in range(n):
    s, a = input().split()
    x = 0 if s == 'F' else 1
    x += 2 if int(a) < 40 else 0
    ans[x] += 1

print(*ans)