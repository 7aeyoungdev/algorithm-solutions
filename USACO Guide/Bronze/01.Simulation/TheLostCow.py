# https://usaco.org/index.php?page=viewproblem2&cpid=735

# x 부터 시작해서 y 까지 지그재그로 이동하며 탐색한다.
# 지그재그는 1, -2, 4, -8, ... 로 이어진다.
# y 에 도착하거나 지나치면 탐색을 종료하고 이동 거리를 출력한다.

import sys
sys.stdin = open("lostcow.in", "r")
sys.stdout = open("lostcow.out", "w")

x, y = map(int, input().split())

ans = 0
step = 1

while True:
    if (x <= y <= x + step) or (x + step <= y <= x):
        ans += abs(y - x)
        break

    ans += abs(step) * 2
    step *= -2

print(ans)