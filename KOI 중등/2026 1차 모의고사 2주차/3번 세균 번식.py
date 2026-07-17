# https://jungol.co.kr/contest/4084/problem/3

'''
# BFS (부분 점수)

import sys
from collections import deque

input = sys.stdin.readline

n, m, k = map(int, input().split())
g = [ [-1] * m for _ in range(n) ]
q = deque()

for i in range(k):
    r, c = map(int, input().split())
    g[r - 1][c - 1] = 0
    q.append( (r - 1, c - 1) )

def bfs():
    d = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]
    ans = 0

    while q:
        x, y = q.popleft()
        ans = max(ans, g[x][y])

        for dx, dy in d:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and g[nx][ny] == -1:
                g[nx][ny] = g[x][y] + 1
                q.append( (nx, ny) )
    
    return ans

print(bfs())
'''