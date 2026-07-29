# https://jungol.co.kr/problem/12372

import sys
input = sys.stdin.readline

n = int(input())

cnt = [0] * (n + 1)
edge = []

for i in range(n - 1):
    u, v = map(int, input().split())
    cnt[u] += 1
    cnt[v] += 1
    edge.append( (u, v) )

def combine(n): # n 개 중에서 2 개 뽑는 경우의 수
    if n < 2:
        return 0
    return n * (n - 1) // 2

ans = 0

for u, v in edge:
    ans += combine(cnt[u] - 1) * combine(cnt[v] - 1) # 서로 연결된 개수 제외

print(ans)