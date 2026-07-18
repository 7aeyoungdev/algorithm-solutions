# https://jungol.co.kr/contest/4088/problem/3

n, dh, db, dg = map(int, input().split())
a = list(map(int, input().split()))

ph = [0] * (n + 1)
pb = [0] * (n + 1)
pg = [0] * (n + 1)
for i in range(1, n + 1):
    ph[i] = ph[i - 1]
    pb[i] = pb[i - 1]
    pg[i] = pg[i - 1]
    
    if a[i - 1] == 1:
        ph[i] += 1
    elif a[i - 1] == 2:
        pb[i] += 1
    elif a[i - 1] == 3:
        pg[i] += 1

ch = []
cb = []
cg = []
for i in range(1, n + 1):
    lh, rh = max(1, i - dh), min(n, i + dh)
    lb, rb = max(1, i - db), min(n, i + db)
    lg, rg = max(1, i - dg), min(n, i + dg)
    
    h = ph[rh] - ph[lh - 1]
    b = pb[rb] - pb[lb - 1]
    g = pg[rg] - pg[lg - 1]
    
    if h > 0:
        ch.append( (h, i) )
    if b > 0:
        cb.append( (b, i) )
    if g > 0:
        cg.append( (g, i) )

ch.sort(reverse = True)
cb.sort(reverse = True)
cg.sort(reverse = True)

ans = (-1, -1, -1)
cnt_max = -1
shop_min = 4

ch, cb, cg = ch[:3], cb[:3], cg[:3]
ch.append( (0, -1) )
cb.append( (0, -1) )
cg.append( (0, -1) )
for h, i in ch:
    for b, j in cb:
        for g, k in cg:
            if i != -1 and (i == j or i == k):
                continue
            if j != -1 and j == k:
                continue

            cnt = h + b + g
            shop = 3 - [i, j, k].count(-1)
            
            if cnt > cnt_max or (cnt == cnt_max and shop < shop_min):
                cnt_max = cnt
                shop_min = shop
                ans = (i, j, k)

print(*ans)