# https://jungol.co.kr/contest/4088/problem/1

n = int(input())
dino = [ list(map(int, input().split())) for _ in range(n) ]

ans = [-1, -1]
dx_min, dv_min = 10**20, 0

for i in range(n - 1):
    if dino[i][1] > dino[i+1][1]: # 따라가는 공룡이 빠를 때
        dx = dino[i+1][0] - dino[i][0] # 거리 차
        dv = dino[i][1] - dino[i+1][1] # 속도 차
        
        if dx * dv_min < dx_min * dv: # dx / dv < dx_min / dv_min 대체
            dx_min, dv_min = dx, dv
            ans = [i + 1, i + 2]

if dv_min == 0:
    print(-1)
else:
    print(*ans)