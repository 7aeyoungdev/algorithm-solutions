# https://jungol.co.kr/problem/21027

import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

c = [0] * (n + 1) # 남은 간식 개수
a = [ [] for _ in range(n + 1) ] # 학생이 좋아하는 간식 번호
g = [ [] for _ in range(n + 1) ] # 간식을 좋아하는 학생 번호
v = [False] * (n + 1)

for i in range(1, n + 1):
    x = list(map(int, input().split()))
    c[i] = x[0]
    a[i] = x[1:]

    for snack in a[i]:
        g[snack].append(i)

q = deque()

for i in range(1, n + 1):
    if c[i] == 1:
        q.append(i)

ans = []

while q:
    x = q.popleft()

    if c[x] != 1: # 이미 가져감
        break

    for snack in a[x]: # 좋아하는 간식 중에서
        if not v[snack]: # 가져가지 않은 간식 번호
            break

    v[snack] = True
    ans.append(x)

    for nx in g[snack]: # x 가 가져갈 간식을 좋아하는 학생들 중에서
        c[nx] -= 1

        if c[nx] == 1: # 남은 간식 개수가 1 인 학생
            q.append(nx)

if len(ans) == n:
    print(*ans)
else:
    print(-1)