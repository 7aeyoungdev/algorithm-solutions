# https://jungol.co.kr/contest/4235/problem/3

n = int(input())
p = [ list(map(int, input().split())) for _ in range(n) ]

p.sort(reverse = True)
p.append([0, 0, 10000])

ans = 0

for i in range(n):
    # left
    for j in range(i + 1, n + 1):
        if p[j][1] <= p[i][1] < p[j][2]:
            ans += p[i][0] - p[j][0]
            break
    # right
    for j in range(i + 1, n + 1):
        if p[j][1] < p[i][2] <= p[j][2]:
            ans += p[i][0] - p[j][0]
            break

print(ans)