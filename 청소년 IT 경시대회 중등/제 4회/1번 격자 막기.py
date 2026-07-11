# https://jungol.co.kr/problem/12364

n = int(input())
g = [ list(map(int, input().split())) for _ in range(2) ]

visit = [ [False] * n for _ in range(2) ]
d = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

from collections import deque

def bfs(sx, sy):
    q = deque()
    q.append( (sx, sy) )
    visit[sx][sy] = True

    while q:
        x, y = q.popleft()
        if x == 1 and y == n - 1:
            return True
        for dx, dy in d:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 2 and 0 <= ny < n:
                if not visit[nx][ny] and g[nx][ny] == 1:
                    q.append( (nx, ny) )
                    visit[nx][ny] = True

    return False

if not bfs(0, 0):
    print(0)
elif 0 in g[0] or 0 in g[1]:
    print(1)
else:
    print(2)