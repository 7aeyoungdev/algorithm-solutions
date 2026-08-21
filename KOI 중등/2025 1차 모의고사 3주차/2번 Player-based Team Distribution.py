# https://jungol.co.kr/contest/2496/problem/3

n = int(input())
a = list(map(int, input().split()))
a.sort(reverse=True)

total = sum(a)
ans = total
s = 0

for i in range(n):
    s += a[i]

    score = i * s + total

    ans = max(ans, score)

print(ans)