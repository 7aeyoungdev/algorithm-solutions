# https://usaco.org/index.php?page=viewproblem2&cpid=855

# 우유를 1 > 2, 2 > 3, 3 > 1 번 순서로 100 번 붓는다.
# 주는 쪽이 비거나 받는 쪽이 가득 찰 때까지만 붓는다.
# 100 번이 끝나고 각 bucket 에 남은 우유의 양을 출력한다.

import sys
sys.stdin = open("mixmilk.in", "r")
sys.stdout = open("mixmilk.out", "w")

c = [0] * 3
m = [0] * 3

for i in range(3):
    c[i], m[i] = map(int, input().split())

for i in range(100):
    give = i % 3
    take = (i + 1) % 3

    milk = min(m[give], c[take] - m[take])

    m[give] -= milk
    m[take] += milk

print(*m, sep = '\n')