# https://jungol.co.kr/problem/8568

n = int(input())
a = input()
b = input()
p1, p3, p5, pp = map(int, input().split())

d = [0] * (n + 1)

def cost(x, end):
    cx = [0] * (end + 5)

    for j in range(end - 1, -1, -1):
        if x[j] == '0':
            cx[j] = cx[j + 1]
        else:
            cx[j] = min(cx[j + 1] + p1, cx[j + 3] + p3, cx[j + 5] + p5)

    return cx

for i in range(1, n + 1):
    # 묶음권 만료 
    ans = pp
    if i >= 4:
        ans += d[i - 4]

    # 1, 3, 5일권 만료
    ca = cost(a, i)
    cb = cost(b, i)

    for j in range(i):
        ans = min(ans, d[j] + ca[j] + cb[j])

    d[i] = ans

print(d[n])