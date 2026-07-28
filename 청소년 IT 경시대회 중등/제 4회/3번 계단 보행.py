# https://jungol.co.kr/problem/12368

import sys
input = sys.stdin.readline

from collections import deque

n, m = map(int, input().split())
g = [ {} for _ in range(n + 1) ] # {가중치 a : 연결된 정점 리스트, 가중치 b : 연결된 정점 리스트}

for i in range(m):
    u, v, w = map(int, input().split())

    if w not in g[u]:
        g[u][w] = []
    g[u][w].append(v)

    if w not in g[v]:
        g[v][w] = []
    g[v][w].append(u)

def move(u, w, d):
    if w not in g[u]: # 계단 가중치가 없으면
        return

    vl = g[u].pop(w) # 해당 가중치로 연결된 정점 리스트, g[u][w] 와 같지만, 중복을 막기 위해 pop
    for v in vl:
        q.append( (v, w, d) )

        if ans[v] == -1:
            ans[v] = d

ans = [-1] * (n + 1)
q = deque() # 정점, 가중치, 거리
q.append( (1, 0, 0) )

while q:
    u, w, d = q.popleft()

    if w == 0: # 가중치가 0 (시작점) 이라면, 연결된 모든 가중치로 이동
        wl = list(g[u]) # u 정점에 연결된 가중치 리스트
        for nw in wl:
            move(u, nw, d + 1)
    else: # 계단 가중치로 이동
        move(u, w - 1, d + 1)
        move(u, w + 1, d + 1)

print(*ans[1:])