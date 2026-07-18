# https://jungol.co.kr/contest/4088/problem/2

from collections import deque

n = int(input())
s = input()
v = [-1] * n  # 아이템 개수

def bfs(sx):
    if s[sx] == '#':
        return -1
    
    cnt = 0
    if s[sx] == '*':
        cnt += 1
    
    q = deque()
    q. append( (sx, cnt, 0) )
    v[sx] = cnt

    while q:
        x, c, t = q.popleft()

        d = [1] # 이동 가능한 거리
        if c > 0:
            d.append(1 + c)

        for dx in d:
            nx = x + dx
            nc = c

            if nx >= n:
                return t + 1
            
            if s[nx] == '#':
                continue

            if s[nx] == '*':
                nc += 1

            if nc > v[nx]:
                q.append( (nx, nc, t + 1) )
                v[nx] = nc
                
    return -1

print(bfs(0))