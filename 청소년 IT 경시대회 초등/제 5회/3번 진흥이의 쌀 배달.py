# https://jungol.co.kr/problem/12373

import sys
sys.setrecursionlimit(2000)

n, k = map(int, input().split())
s = [0] + list(map(int, input().split()))

g = [ [] for _ in range(n + 1) ]
for _ in range(n):
    u, v, t = map(int, input().split())
    g[u].append( (v, t) )
    g[v].append( (u, t) )

ans = 0

def dfs(x, p):
    global ans
    
    rice = s[x]
    
    for nx, t in g[x]:
        if nx != p:
            r = dfs(nx, x)
            
            cnt = (r + k - 1) // k # 왕복 횟수
            ans += t * 2 * cnt # t 시간 왕복
            
            rice += r
            
    return rice

dfs(0, -1)

print(ans)