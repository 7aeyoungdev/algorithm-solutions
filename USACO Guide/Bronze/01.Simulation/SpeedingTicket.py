# https://usaco.org/index.php?page=viewproblem2&cpid=568

# 제한 속도와 실제 속도를 비교해, 초과한 속도의 최댓값을 출력한다.

import sys
sys.stdin = open("speeding.in", "r")
sys.stdout = open("speeding.out", "w")

n, m = map(int, input().split())

limit = []
speed = []

for i in range(n):
    l, s = map(int, input().split())
    limit += [s] * l

for i in range(m):
    l, s = map(int, input().split())
    speed += [s] * l

ans = 0
for i in range(100):
    ans = max(ans, speed[i] - limit[i])

print(ans)