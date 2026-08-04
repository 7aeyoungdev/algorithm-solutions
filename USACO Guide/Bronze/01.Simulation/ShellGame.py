# https://usaco.org/index.php?page=viewproblem2&cpid=891

# 조개 껍데기의 위치를 swap 하고, 조약돌의 위치를 guess 한다.
# 정답 횟수의 최댓값을 출력한다.

import sys
sys.stdin = open("shell.in", "r")
sys.stdout = open("shell.out", "w")

n = int(input())
swap = [ list(map(int, input().split())) for _ in range(n) ]

ans = 0

for peb in range(1, 4):
    shell = [False] * 4
    shell[peb] = True
    cnt = 0

    for a, b, g in swap:
        shell[a], shell[b] = shell[b], shell[a]

        if shell[g]:
            cnt += 1

    ans = max(ans, cnt)

print(ans)