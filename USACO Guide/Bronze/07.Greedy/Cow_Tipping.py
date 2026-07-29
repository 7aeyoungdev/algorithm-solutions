# https://usaco.org/index.php?page=viewproblem2&cpid=689

import sys

sys.stdin = open('cowtip.in', 'r')
sys.stdout = open('cowtip.out', 'w')

n = int(input())
g = [ list(map(int, input())) for _ in range(n) ]

ans = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if g[i][j] == 1:
            ans += 1
            for r in range(i + 1):
                for c in range(j + 1):
                    g[r][c] = 1 - g[r][c]

print(ans)