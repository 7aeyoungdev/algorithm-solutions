# https://jungol.co.kr/contest/2483/problem/2

n = list(input())

ans = -1

for i in range(len(n)):
    for j in range(i + 1, len(n)):
        n[i], n[j] = n[j], n[i]

        s = ''
        for c in n:
            s += c
        x = int(s)

        ans = max(ans, x)
        
        n[i], n[j] = n[j], n[i]

print(ans)