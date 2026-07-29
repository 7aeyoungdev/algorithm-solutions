# https://usaco.org/index.php?page=viewproblem2&cpid=663

import sys

sys.stdin = open('square.in', 'r')
sys.stdout = open('square.out', 'w')

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

xl = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
yl = max(y1, y2, y3, y4) - min(y1, y2, y3, y4)

l = max(xl, yl)

print(l * l)