# https://jungol.co.kr/contest/4096/problem/3

from collections import deque

r, c = map(int, input().split())
g = [ list(input()) for _ in range(r) ]

cnt = 0
q = deque()

for i in range(r):
    cnt += g[i].count('.')
    if g[i][0] == '.':
        g[i][0] = 1
        q.append( (i, 0) )

d = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
l = -1
while q:
    x, y = q.popleft()
    if y == c - 1:
        l = g[x][y]
        break

    for dx, dy in d:
        nx, ny = x + dx, y + dy

        if 0 <= nx < r and 0 <= ny < c:
            if g[nx][ny] == '.':
                g[nx][ny] = g[x][y] + 1
                q.append( (nx, ny) )

print(cnt - l)