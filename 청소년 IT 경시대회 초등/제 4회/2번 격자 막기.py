# https://jungol.co.kr/problem/12364

from collections import deque

n = int(input())
g = [ list(map(int, input().split())) for _ in range(2) ]
d = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

block = 0 in g[0] or 0 in g[1]

def bfs(sx, sy):
    q = deque()
    q.append( (sx, sy) )

    while q:
        x, y = q.popleft()
        if x == 1 and y == n - 1:
            return True
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < n:
                if g[nx][ny] == 1:
                    g[nx][ny] = 0
                    q.append( (nx, ny) )

    return False

if not bfs(0, 0):
    print(0)
elif block:
    print(1)
else:
    print(2)