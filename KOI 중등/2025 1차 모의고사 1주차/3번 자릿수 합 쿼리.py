# https://jungol.co.kr/contest/2484/problem/3

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
a = [0] + list(map(int, input().split()))

seg = [0] * (4 * n + 1)
top = [0] * (4 * n + 1)

def digit(x):
    return sum(map(int, str(x)))

def build(node, st, ed):
    if st == ed:
        seg[node] = a[st]
        top[node] = a[st]
        return

    lc, rc = node * 2, node * 2 + 1
    mid = (st + ed) // 2
    build(lc, st, mid)
    build(rc, mid + 1, ed)

    seg[node] = seg[lc] + seg[rc]
    top[node] = max(top[lc], top[rc])

def update(node, st, ed, l, r):
    if r < st or ed < l:
        return

    if top[node] < 10:
        return

    if st == ed:
        a[st] = digit(a[st])
        seg[node] = a[st]
        top[node] = a[st]
        return

    lc, rc = node * 2, node * 2 + 1
    mid = (st + ed) // 2
    update(lc, st, mid, l, r)
    update(rc, mid + 1, ed, l, r)

    seg[node] = seg[lc] + seg[rc]
    top[node] = max(top[lc], top[rc])

def query(node, st, ed, l, r):
    if r < st or ed < l:
        return 0 # 원소의 합, 덧셈 항등원, 최솟값을 구한다면 10**20 등

    if l <= st and ed <= r:
        return seg[node]

    lc, rc = node * 2, node * 2 + 1
    mid = (st + ed) // 2
    lans = query(lc, st, mid, l, r)
    rans = query(rc, mid + 1, ed, l, r)

    return lans + rans # 원소의 합

build(1, 1, n)

ans = []

for i in range(q):
    x, l, r = map(int, input().split())
    if x == 1:
        update(1, 1, n, l, r)
    else:
        ans.append(query(1, 1, n, l, r))

print(*ans, sep = '\n')