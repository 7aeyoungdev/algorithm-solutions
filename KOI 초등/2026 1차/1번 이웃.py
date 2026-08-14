# https://jungol.co.kr/problem/12498

n, k1, k2 = map(int, input().split())
s = list(map(int, input().split()))

ans = []

for i in range(n):
    cnt = 0

    for j in range(n):
        dist = abs(i - j)

        if s[i] == s[j] and dist <= k1:
            cnt += 1
        elif s[i] != s[j] and dist <= k2:
            cnt += 1

    ans.append(cnt - 1)

print(*ans)