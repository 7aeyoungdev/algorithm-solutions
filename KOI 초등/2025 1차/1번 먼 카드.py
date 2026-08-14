# https://jungol.co.kr/problem/8565

n = int(input())
x = list(map(int, input().split()))

ans = 0

for i in range(2 * n):
    for j in range(i + 1, 2 * n):
        if x[i] == x[j]:
            ans  = max(ans, j - i - 1)
            break

print(ans)