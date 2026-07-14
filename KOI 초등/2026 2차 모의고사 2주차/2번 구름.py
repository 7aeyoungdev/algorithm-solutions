# https://jungol.co.kr/contest/4235/problem/2

h, w = map(int, input().split())
g = [ list(input()) for _ in range(h) ]

for i in range(h):
    for j in range(w):
        if g[i][j] == '.':
            g[i][j] = -1
        else:
            g[i][j] = 0
    
    for j in range(1, w):
        if g[i][j] < 0 and g[i][j - 1] >= 0:
            g[i][j] = g[i][j - 1] + 1

for r in g:
    print(*r)