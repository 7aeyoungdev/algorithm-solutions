# https://jungol.co.kr/contest/4087/problem/2

n, d = map(int, input().split())
a = list(map(int, input().split()))

ph = [0] * (n + 1)
pb = [0] * (n + 1)
for i in range(1, n + 1):
    ph[i] = ph[i - 1]
    pb[i] = pb[i - 1]
    
    if a[i - 1] == 1:
        ph[i] += 1
    elif a[i - 1] == 2:
        pb[i] += 1

ch = []
cb = []
for i in range(1, n + 1):
    l = max(1, i - d)
    r = min(n, i + d)
    
    h = ph[r] - ph[l - 1]
    b = pb[r] - pb[l - 1]
    
    if h > 0:
        ch.append( (h, i) )
    if b > 0:
        cb.append( (b, i) )

ch.sort(reverse = True)
cb.sort(reverse = True)

ans = (-1, -1)
cnt_max = -1
shop_min = 3

ch, cb = ch[:2], cb[:2]
ch.append( (0, -1) )
cb.append( (0, -1) )
for h, i in ch:
    for b, j in cb:
        if i != -1 and i == j:
            continue

        cnt = h + b
        shop = 2 - [i, j].count(-1)
        
        if cnt > cnt_max or (cnt == cnt_max and shop < shop_min):
            cnt_max = cnt
            shop_min = shop
            ans = (i, j)

print(*ans)