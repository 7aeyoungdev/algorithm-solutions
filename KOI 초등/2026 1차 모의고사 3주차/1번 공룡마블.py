# https://jungol.co.kr/contest/4087/problem/1

from collections import deque

n = int(input())
a = list(map(int, input().split()))
v = [-1] * n

def bfs(sx):
    q = deque()
    q.append(sx)
    v[sx] = 0

    while q:
        x = q.popleft()

        nx = x + a[x]
        if 0 <= nx < n and v[nx] == -1:
            q.append(nx)
            v[nx] = v[x] + 1

bfs(0)

print(v[n - 1])