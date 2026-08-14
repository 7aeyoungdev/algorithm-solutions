# https://jungol.co.kr/problem/8604

n = int(input())
x = [-1] + list(map(int, input().split()))

ans = 0

for i in range(n):
    d = x[i + 1] - x[i]
    if d == 1:
        print(-1)
        break

    ans += (d - 1) // 2 + 1
else:
    print(ans)