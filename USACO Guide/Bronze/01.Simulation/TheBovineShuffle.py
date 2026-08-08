# https://usaco.org/index.php?page=viewproblem2&cpid=760

# 3 번 shuffle 전의 id 를 순서대로 출력한다.

import sys
sys.stdin = open("shuffle.in", "r")
sys.stdout = open("shuffle.out", "w")

n = int(input())
a = list(map(int, input().split()))
id = list(map(int, input().split()))

for s in range(3):
    prev_id = [0] * n

    for i in range(n):
        prev_id[i] = id[a[i] - 1]

    id = prev_id

print(*id, sep = '\n')