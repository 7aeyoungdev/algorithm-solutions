# https://jungol.co.kr/problem/8567

n = int(input())

con = [] # y = c, #c = y
inc = [] # y = x + c, c = y - x
dec = [] # y = -x + c, c = y + x

for i in range(n):
    x, y = map(int, input().split())

    con.append(y)
    inc.append(y - x)
    dec.append(y + x)

ans = []

# 정방향 △
# con 최소, inc, dec 최대

# left : y = con 일 때, 증가 함수에서 x 의 값
# y = x + inc, con = x + inc, x = con - inc
l = min(con) - max(inc)

# right : y = con 일 때, 감소 함수에서 x 의 값
# y = -x + dec, con = -x + dec, x = -con + dec
r = -min(con) + max(dec)

ans.append(r - l)

# 역방향 ▽
# con 최대, inc, dec 최소

# left : y = con 일 때, 감소 함수에서 x 의 값
# y = -x + dec, con = -x + dec, x = -con + dec
l = -max(con) + min(dec)

# right : y = con 일 때, 증가 함수에서 x 의 값
# y = x + inc, con = x + inc, x = con - inc
r = max(con) - min(inc)

ans.append(r - l)

print(min(ans))