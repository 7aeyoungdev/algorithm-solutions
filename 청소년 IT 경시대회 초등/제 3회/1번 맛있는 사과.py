# https://jungol.co.kr/problem/12357

import sys
input = sys.stdin.readline

n, q = map(int, input().split())
t = list(map(int, input().split()))
s = list(map(int, input().split()))

apple = [0] * n
for i in range(n):
    apple[i] = (t[i], s[i]) # 맛, 크기
apple.sort(reverse=True)

ps = []
for i in range(q):
    p = int(input())
    ps.append( (p, i) ) # 기준 맛, 원래 순서
ps.sort(reverse=True)

ans = [0] * q
idx = 0
s_max = -1
cnt = 0

for p, i in ps:
    while idx < n and apple[idx][0] >= p:
        s_cur = apple[idx][1]
        
        if s_cur > s_max:
            s_max = s_cur
            cnt = 1
        elif s_cur == s_max:
            cnt += 1
            
        idx += 1
        
    ans[i] = cnt

print(*ans, sep = '\n')