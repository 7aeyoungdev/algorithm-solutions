# https://usaco.org/index.php?page=viewproblem2&cpid=856

# 시작 시간, 종료 시간, 필요한 양동이 수 가 주어질 때, 준비해야 하는 총 양동이의 최솟값을 출력한다.
# 시간이 겹치지 않으면 양동이를 재사용할 수 있다.

import sys
sys.stdin = open("blist.in", "r")
sys.stdout = open("blist.out", "w")

n = int(input())

bucket = [0] * 1001

for i in range(n):
    s, t, b = map(int, input().split())
    for time in range(s, t + 1):
        bucket[time] += b

print(max(bucket))