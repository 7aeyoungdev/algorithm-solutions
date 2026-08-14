# https://jungol.co.kr/problem/8608

n, k, c = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

p = [0] * (n + 1)
for i in range(n):
    p[i + 1] = p[i] + a[i]

s = 0
ans = []

for x in range(1, c + 1):
    while s < n - k:
        if p[s + 1] > x:
            break

        s += 1
    
    ans.append(p[s + k] - p[s])

print(*ans, sep = '\n')