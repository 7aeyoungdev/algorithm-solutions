# https://jungol.co.kr/problem/12491

import sys
import bisect
input = sys.stdin.readline

n, k1, k2 = map(int, input().split())
pos = []
school = []
pos_group = {}

for i in range(n):
    x, s = map(int, input().split())
    pos.append(x)
    school.append(s)

    if s not in pos_group:
        pos_group[s] = []
    pos_group[s].append(x)

pos_sort = pos.copy()
pos_sort.sort()
for g in pos_group:
    pos_group[g].sort()

ans = []

def count(l, x, k):
    return bisect.bisect_right(l, x + k) - bisect.bisect_left(l, x - k)

for i in range(n):
    a = count(pos_sort, pos[i], k2)
    b = count(pos_group[school[i]], pos[i], k1)
    c = count(pos_group[school[i]], pos[i], k2)

    ans.append(a + b - c - 1)

print(*ans)